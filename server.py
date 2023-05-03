#!/usr/bin/python3
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
print("Welcome! This is a simple server on python http.")
print("Now you must choose parametres of server:")
address = str(input("Input address: (Default: localhost)\n"))
port = str(input("Input port: (Dfeault: 8000)\n"))
if address=="":
    address = "localhost"
if port == "":
    port = 8000
else:
    port = int(port)
if not (0<=port<=65535):
    print("Invalid Port! Choosed 8000\n")
    port = 8000
server_address = (address, port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
try:
    print("Server started")
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
    print("\nSTOPPED! SERVER IS SHUTING DOWN...\n")
except Exception:
    httpd.shutdown()
    print("\nERROR! SERVER IS SHUTTING DOWN...\n")
