#!/usr/bin/python3
from http import server
import os
import socket
import netifaces
from http.server import SimpleHTTPRequestHandler, HTTPServer
iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
print("Welcome! This is a simple server on python http.")
print("Now you must choose parametres of server:")
address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
port = str(input("Input port: (Default: 8000)\n"))

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
    print("You can connect to this PC by address:\n"+str(address)+":"+str(port))
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
    print("\nSTOPPED! SERVER IS SHUTING DOWN...\n")
except Exception:
    httpd.shutdown()
    print("\nERROR! SERVER IS SHUTTING DOWN...\n")
