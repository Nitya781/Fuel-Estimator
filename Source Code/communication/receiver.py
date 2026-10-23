"""
=========================================================
UDP Receiver
---------------------------------------------------------
Receives UDP packets from FlightGear.

Author : HAL Fuel Estimation Project
=========================================================
"""

import socket


class UDPReceiver:

    """
    Receives UDP packets from FlightGear Generic Protocol.
    """

    def __init__(
        self,
        ip_address: str = "127.0.0.1",
        port: int = 5500,
        buffer_size: int = 4096
    ):

        self.ip_address = ip_address
        self.port = port
        self.buffer_size = buffer_size

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        self.socket.bind(
            (
                self.ip_address,
                self.port
            )
        )

        print(
            f"[Receiver] Listening on "
            f"{self.ip_address}:{self.port}"
        )

    # ==================================================
    # Receive one FlightGear packet
    # ==================================================

    def receive(self) -> str:

        """
        Waits for one UDP packet and returns it as a string.

        Returns
        -------
        str
            Comma-separated FlightGear packet.
        """

        try:

            packet, _ = self.socket.recvfrom(
                self.buffer_size
            )

            decoded = packet.decode("utf-8").strip()
            print(decoded)
            return decoded

        except Exception as error:

            print(
                f"[Receiver Error] {error}"
            )

            return ""

    # ==================================================
    # Close Socket
    # ==================================================

    def close(self):

        """
        Closes the UDP socket.
        """

        self.socket.close()

        print("[Receiver] Socket Closed")
