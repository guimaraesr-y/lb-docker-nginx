#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, os

SERVER_ID = os.getenv("SERVER_ID", 1)
SERVER_COLOR = os.getenv("SERVER_COLOR", "#fff")

host = "0.0.0.0"
port = 8080

def get_template():
    template = f"""
        <html>
            <head>
                <title>Server {SERVER_ID}</title>
                <style>
                    body {{
                        font-family: 'Segoe UI', sans-serif;
                        text-align: center;
                        margin-top: 40vh;
                        background-color: {SERVER_COLOR};
                    }}
                </style>
            </head>
            <body>
                <h1>Welcome! Server {SERVER_ID}</h1>
                <p>It is now {time.asctime()}</p>
            </body>
        </html>
    """
    
    return template


class LBServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(get_template(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((host, port), LBServer)
    print(f"Server started http://{host}:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
