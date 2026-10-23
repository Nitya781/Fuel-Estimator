"""
=========================================================
Fuel State Model
---------------------------------------------------------
Tracks fuel consumption throughout the flight.

Author : HAL Fuel Estimation Project
=========================================================
"""


class FuelStateModel:

    """
    Maintains aircraft fuel state.
    """

    def __init__(
        self,
        initial_fuel_kg: float,
        fuel_capacity_kg: float
    ):

        self.initial_fuel_kg = initial_fuel_kg
        self.fuel_capacity_kg = fuel_capacity_kg

        self.fuel_consumed_kg = 0.0
        self.fuel_remaining_kg = initial_fuel_kg

    # ==================================================
    # Update Fuel State
    # ==================================================

    def update(
        self,
        fuel_flow_kg_sec: float,
        delta_time_sec: float
    ):

        """
        Updates fuel state using numerical integration.
        """

        consumed = fuel_flow_kg_sec * delta_time_sec

        self.fuel_consumed_kg += consumed

        self.fuel_remaining_kg = (
            self.initial_fuel_kg -
            self.fuel_consumed_kg
        )

        if self.fuel_remaining_kg < 0:
            self.fuel_remaining_kg = 0.0

    # ==================================================
    # Fuel Percentage
    # ==================================================

    def fuel_percentage(self):

        if self.fuel_capacity_kg <= 0:
            return 0.0

        return (
            self.fuel_remaining_kg /
            self.fuel_capacity_kg
        ) * 100.0

    # ==================================================
    # Get Current Fuel State
    # ==================================================

    def get_state(self):

        return {

            "fuel_consumed_kg":
                self.fuel_consumed_kg,

            "fuel_remaining_kg":
                self.fuel_remaining_kg,

            "fuel_percentage":
                self.fuel_percentage()
        }
