from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = 8000

class FuelDashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        return super().do_GET()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    server = HTTPServer(("0.0.0.0", PORT), FuelDashboardHandler)

    print("----------------------------------------")
    print(" HAL Fuel Estimation System")
    print("----------------------------------------")
    print(f" Dashboard running at:")
    print(f" http://localhost:{PORT}")
    print("----------------------------------------")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")

    server.server_close()
