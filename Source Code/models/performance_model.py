"""
=========================================================
Performance Model
---------------------------------------------------------
Computes aircraft fuel performance parameters.

Author : HAL Fuel Estimation Project
=========================================================
"""


class PerformanceModel:

    def calculate_endurance(
        self,
        fuel_remaining_kg,
        fuel_flow_kg_hr
    ):

        if fuel_flow_kg_hr <= 0:
            return 0.0

        return fuel_remaining_kg / fuel_flow_kg_hr

    def calculate_range(
        self,
        endurance_hr,
        true_airspeed_kt
    ):

        return endurance_hr * true_airspeed_kt

    def calculate_fuel_at_landing(
        self,
        fuel_remaining_kg,
        distance_nm,
        true_airspeed_kt,
        fuel_flow_kg_hr
    ):

        if true_airspeed_kt <= 0:
            return fuel_remaining_kg

        flight_time_hr = distance_nm / true_airspeed_kt

        required_fuel = (
            flight_time_hr *
            fuel_flow_kg_hr
        )

        fuel_at_landing = (
            fuel_remaining_kg -
            required_fuel
        )

        return max(fuel_at_landing, 0.0)

    # -------------------------------------------------
    # Reserve Fuel
    # -------------------------------------------------

    def calculate_reserve_fuel(
        self,
        reserve_fuel_kg
    ):

        return reserve_fuel_kg

    # -------------------------------------------------
    # Bingo Fuel
    # -------------------------------------------------

    def calculate_bingo_fuel(
        self,
        distance_to_base_nm,
        cruise_speed_kt,
        fuel_flow_kg_hr,
        reserve_fuel_kg,
        bingo_margin_kg
    ):

        if cruise_speed_kt <= 0:
            return reserve_fuel_kg + bingo_margin_kg

        return_time_hr = (
            distance_to_base_nm /
            cruise_speed_kt
        )

        return_fuel = (
            return_time_hr *
            fuel_flow_kg_hr
        )

        return (
            return_fuel +
            reserve_fuel_kg +
            bingo_margin_kg
        )
