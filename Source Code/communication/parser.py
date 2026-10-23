"""
=========================================================
FlightGear Packet Parser
---------------------------------------------------------
Converts a comma-separated FlightGear UDP packet into
a FlightData object.

Packet Format (13 Parameters)

1. Time (sec)
2. Latitude (deg)
3. Longitude (deg)
4. Altitude (ft)
5. Heading (deg)
6. Mach
7. True Airspeed (kt)
8. Outside Air Temperature (degC)
9. Throttle (0-1)
10. Afterburner (0/1)
11. Engine Thrust (lbf)
12. Current Fuel (kg)
13. Distance to Waypoint (NM)

Author : HAL Fuel Estimation Project
=========================================================
"""

from models.flight_data import FlightData


class FlightDataParser:

    EXPECTED_PARAMETERS = 13

    def parse(self, packet: str) -> FlightData:

        values = packet.strip().split(",")

        if len(values) != self.EXPECTED_PARAMETERS:
            raise ValueError(
                f"Expected {self.EXPECTED_PARAMETERS} parameters, "
                f"received {len(values)}"
            )

        flight_data = FlightData()

        # -------------------------------------------------
        # Time
        # -------------------------------------------------

        flight_data.time = float(values[0])

        # -------------------------------------------------
        # Position
        # -------------------------------------------------

        flight_data.latitude = float(values[1])
        flight_data.longitude = float(values[2])

        flight_data.altitude_ft = float(values[3])
        flight_data.heading_deg = float(values[4])

        # -------------------------------------------------
        # Aircraft Performance
        # -------------------------------------------------

        flight_data.mach = float(values[5])

        flight_data.true_airspeed_kt = float(values[6])

        flight_data.temperature_degC = float(values[7])

        # -------------------------------------------------
        # Engine
        # -------------------------------------------------

        flight_data.throttle = float(values[8])

        flight_data.afterburner = int(values[9]) == 1

        flight_data.thrust_lbf = float(values[10])

        # -------------------------------------------------
        # Fuel
        # -------------------------------------------------

        flight_data.current_fuel_kg = float(values[11])

        # -------------------------------------------------
        # Navigation
        # -------------------------------------------------

        flight_data.distance_to_waypoint_nm = float(values[12])

        return flight_data
