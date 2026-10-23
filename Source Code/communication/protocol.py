"""
=========================================================
FlightGear Communication Protocol
---------------------------------------------------------
Contains communication constants for the FlightGear UDP
interface.

Keeping these values in one location makes the communication
layer easy to configure and maintain.

Author : HAL Fuel Estimation Project
=========================================================
"""


class FlightGearProtocol:
    """
    Stores all FlightGear communication parameters.
    """

    # =====================================================
    # Network Configuration
    # =====================================================

    IP_ADDRESS = "127.0.0.1"

    PORT = 5500

    BUFFER_SIZE = 4096

    # =====================================================
    # Packet Configuration
    # =====================================================

    ENCODING = "utf-8"

    FIELD_SEPARATOR = ","

    # =====================================================
    # FlightGear Update Rate
    # =====================================================

    UPDATE_RATE_HZ = 20

    TIME_STEP_SEC = 0.05
