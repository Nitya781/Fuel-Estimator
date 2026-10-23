"""
=========================================================
Fuel Estimation Engine

Coordinates the complete fuel estimation process.

Pipeline

FlightData
    ↓
SFC Model
    ↓
Fuel Flow Model
    ↓
Fuel State Model
    ↓
Performance Model
    ↓
Results

Author : HAL Fuel Estimation Project
=========================================================
"""

from models.sfc_model import SFCModel
from models.fuel_flow_model import FuelFlowModel
from models.fuel_state_model import FuelStateModel
from models.performance_model import PerformanceModel
from models.results import Results


class FuelEstimator:

    def __init__(
        self,
        dry_sfc,
        afterburner_sfc,
        initial_fuel_kg,
        fuel_capacity_kg,
        reserve_fuel_kg,
        bingo_margin_kg
    ):

        self.results = Results()

        # ---------------------------------------------
        # Models
        # ---------------------------------------------

        self.sfc_model = SFCModel(
            dry_sfc=dry_sfc,
            afterburner_sfc=afterburner_sfc
        )

        self.fuel_flow_model = FuelFlowModel()

        self.fuel_state_model = FuelStateModel(
            initial_fuel_kg,
            fuel_capacity_kg
        )

        self.performance_model = PerformanceModel()

        # ---------------------------------------------
        # Mission Parameters
        # ---------------------------------------------

        self.reserve_fuel_kg = reserve_fuel_kg
        self.bingo_margin_kg = bingo_margin_kg

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self, flight_data):

        # ==================================================
        # STEP 1 : Specific Fuel Consumption
        # ==================================================

        sfc = self.sfc_model.calculate(
            mach=flight_data.mach,
            throttle=flight_data.throttle,
            ambient_temperature_degC=flight_data.temperature_degC,
            afterburner=flight_data.afterburner
        )

        self.results.sfc = sfc

        # ==================================================
        # STEP 2 : Fuel Flow
        # ==================================================

        fuel_flow = self.fuel_flow_model.calculate(
            thrust_lbf=flight_data.thrust_lbf,
            sfc=sfc
        )

        self.results.fuel_flow_lbs_hr = fuel_flow["fuel_flow_lbs_hr"]
        self.results.fuel_flow_kg_hr = fuel_flow["fuel_flow_kg_hr"]
        self.results.fuel_flow_kg_min = fuel_flow["fuel_flow_kg_min"]
        self.results.fuel_flow_kg_sec = fuel_flow["fuel_flow_kg_sec"]

        # ==================================================
        # STEP 3 : Fuel State
        # ==================================================

        self.fuel_state_model.update(
            fuel_flow_kg_sec=fuel_flow["fuel_flow_kg_sec"],
            delta_time_sec=flight_data.delta_time
        )

        state = self.fuel_state_model.get_state()

        self.results.fuel_consumed_kg = state["fuel_consumed_kg"]
        self.results.fuel_remaining_kg = state["fuel_remaining_kg"]
        self.results.fuel_percentage = state["fuel_percentage"]

        # ==================================================
        # STEP 4 : Endurance
        # ==================================================

        self.results.endurance_hr = (
            self.performance_model.calculate_endurance(
                self.results.fuel_remaining_kg,
                self.results.fuel_flow_kg_hr
            )
        )

        # ==================================================
        # STEP 5 : Range
        # ==================================================

        self.results.range_nm = (
            self.performance_model.calculate_range(
                self.results.endurance_hr,
                flight_data.true_airspeed_kt
            )
        )

        # ==================================================
        # STEP 6 : Fuel at Landing
        # ==================================================

        self.results.fuel_at_landing_kg = (
            self.performance_model.calculate_fuel_at_landing(
                self.results.fuel_remaining_kg,
                flight_data.distance_to_waypoint_nm,
                flight_data.true_airspeed_kt,
                self.results.fuel_flow_kg_hr
            )
        )

        # ==================================================
        # STEP 7 : Reserve Fuel
        # ==================================================

        self.results.reserve_fuel_kg = (
            self.performance_model.calculate_reserve_fuel(
                self.reserve_fuel_kg
            )
        )

        # ==================================================
        # STEP 8 : Bingo Fuel
        # ==================================================

        self.results.bingo_fuel_kg = (
            self.performance_model.calculate_bingo_fuel(
                flight_data.distance_to_waypoint_nm,
                flight_data.true_airspeed_kt,
                self.results.fuel_flow_kg_hr,
                self.results.reserve_fuel_kg,
                self.bingo_margin_kg
            )
        )

        return self.results
