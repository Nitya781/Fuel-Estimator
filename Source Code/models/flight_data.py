"""
=========================================================
Flight Data Model
---------------------------------------------------------

=========================================================
Flight Data Model
---------------------------------------------------------
Stores one complete FlightGear telemetry frame.

This object is populated by the FlightGear Parser and
passed to the Fuel Estimation Engine.

Author : HAL Fuel Estimation Project
=========================================================
"""


class FlightData:

    def __init__(self):

        # ==================================================
        # Time
        # ==================================================

        self.time = 0.0
        self.delta_time = 0.05

        # ==================================================
        # Position
        # ==================================================

        self.latitude = 0.0
        self.longitude = 0.0

        self.altitude_ft = 0.0
        self.heading_deg = 0.0

        # ==================================================
        # Aircraft Performance
        # ==================================================

        self.mach = 0.0
        self.true_airspeed_kt = 0.0
        self.temperature_degC = 15.0

        # ==================================================
        # Engine
        # ==================================================

        self.throttle = 0.0
        self.afterburner = False
        self.thrust_lbf = 0.0

        # ==================================================
        # Fuel
        # ==================================================

        self.current_fuel_kg = 0.0

        # ==================================================
        # Navigation
        # ==================================================

        self.distance_to_waypoint_nm = 0.0
