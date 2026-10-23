"""
=========================================================
Fuel Estimation Results

Stores every calculated parameter of the fuel estimation
system.

Every engineering model updates this object.

Author : HAL Fuel Estimation Project
=========================================================
"""


class Results:

    def __init__(self):

        # -----------------------------
        # SFC
        # -----------------------------

        self.sfc = 0.0

        # -----------------------------
        # Fuel Flow
        # -----------------------------

        self.fuel_flow_lbs_hr = 0.0
        self.fuel_flow_kg_hr = 0.0
        self.fuel_flow_kg_min = 0.0
        self.fuel_flow_kg_sec = 0.0

        # -----------------------------
        # Fuel State
        # -----------------------------

        self.fuel_consumed_kg = 0.0
        self.fuel_remaining_kg = 0.0
        self.fuel_percentage = 0.0

        # -----------------------------
        # Performance
        # -----------------------------

        self.endurance_hr = 0.0
        self.range_nm = 0.0
        self.fuel_at_landing_kg = 0.0
        self.reserve_fuel_kg = 0.0
        self.bingo_fuel_kg = 0.0
