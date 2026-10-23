from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys
import os
import threading
import time


# -------------------------------------------------
# Allow project imports
# -------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(PROJECT_ROOT)


from core.fuel_estimator import FuelEstimator
from communication.receiver import UDPReceiver
from communication.parser import FlightDataParser


PORT = 8001


# -------------------------------------------------
# Fuel Engine
# -------------------------------------------------

estimator = FuelEstimator(
    dry_sfc=0.8,
    afterburner_sfc=1.5,
    initial_fuel_kg=5000,
    fuel_capacity_kg=5000,
    reserve_fuel_kg=500,
    bingo_margin_kg=100
)


# -------------------------------------------------
# Latest result storage
# -------------------------------------------------

latest_results = {

    "fuel_remaining": 0,
    "fuel_flow": 0,
    "sfc": 0,

    "endurance": 0,
    "range": 0,

    "fuel_landing": 0,

    "reserve": 500,
    "bingo": 0,

    "status": "WAITING FOR UDP"
}


# -------------------------------------------------
# UDP Processing Thread
# -------------------------------------------------

def udp_loop():

    receiver = UDPReceiver()

    parser = FlightDataParser()


    print("[API] Waiting for FlightGear UDP data...")


    while True:

        packet = receiver.receive()


        if packet:

            try:

                flight_data = parser.parse(packet)


                results = estimator.update(
                    flight_data
                )


                latest_results.update({

                    "fuel_remaining":
                        round(
                            results.fuel_remaining_kg,
                            2
                        ),

                    "fuel_flow":
                        round(
                            results.fuel_flow_kg_hr,
                            2
                        ),

                    "sfc":
                        round(
                            results.sfc,
                            4
                        ),


                    "endurance":
                        round(
                            results.endurance_hr,
                            2
                        ),


                    "range":
                        round(
                            results.range_nm,
                            2
                        ),


                    "fuel_landing":
                        round(
                            results.fuel_at_landing_kg,
                            2
                        ),


                    "reserve":
                        round(
                            results.reserve_fuel_kg,
                            2
                        ),


                    "bingo":
                        round(
                            results.bingo_fuel_kg,
                            2
                        ),


                    "status":
                        "NORMAL"

                })


            except Exception as error:

                print(
                    "[Processing Error]",
                    error
                )


        time.sleep(0.01)



# -------------------------------------------------
# HTTP API
# -------------------------------------------------

class FuelAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/api":

            response = json.dumps(
                latest_results
            )


            self.send_response(200)

            self.send_header(
                "Content-type",
                "application/json"
            )

            self.send_header(
                "Access-Control-Allow-Origin",
                "*"
            )

            self.end_headers()


            self.wfile.write(
                response.encode()
            )


        else:

            self.send_response(404)

            self.end_headers()



# -------------------------------------------------
# Main
# -------------------------------------------------

if __name__ == "__main__":


    thread = threading.Thread(
        target=udp_loop,
        daemon=True
    )

    thread.start()


    server = HTTPServer(
        ("0.0.0.0", PORT),
        FuelAPIHandler
    )


    print("--------------------------------")
    print(" HAL Fuel API running")
    print("--------------------------------")
    print(
        f"API: http://localhost:{PORT}/api"
    )


    try:

        server.serve_forever()


    except KeyboardInterrupt:

        pass


    server.server_close()
