import socket
import time


TARGET_IP = "127.0.0.1"
TARGET_PORT = 5500


sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)


while True:

    packet = (
        "100.0,"
        "13.0345,"
        "77.5632,"
        "15000,"
        "270,"
        "0.82,"
        "450,"
        "15,"
        "0.75,"
        "0,"
        "10500,"
        "3000,"
        "80"
    )


    sock.sendto(
        packet.encode(),
        (TARGET_IP, TARGET_PORT)
    )


    print("Sent:", packet)

    time.sleep(0.05)
