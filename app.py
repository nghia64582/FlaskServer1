from flask import Flask
from flask import request
import json
import time
from datetime import datetime as dt
from logger import Logger
import random as rd
from config import *

app = Flask(__name__)
logger = Logger()
logger.debug("Server start at {}".format(dt.now().strftime("%H:%M:%S")))
app.run(debug = True)
#minor fix 1

def saveDictToJsonFile(data, jsonFile):
    with open(jsonFile, 'w') as outfile:
        json.dump(data, outfile, indent = 4)

def getDictByJson(jsonFile):
    return json.load(open(jsonFile))

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    global logger
    if request.content_type == "application/json" and request.method == "POST":
        logger.debug("Request {} with json {}".format(request.method, request.json))
        if request.json.get("num") != None:
            num = int(request.json.get("num"))
            data = {"a": [i for i in range(num)]}
            saveDictToJsonFile(data, "data1.json")
            logger.debug("IP {} create json with size {}".format(request.remote_addr, num))
            return "Create json with size {}".format(num)
        else:
            logger.debug("POST request without 'num' key.")
            return "Json do not have key <num>"
    elif request.method == "GET":
        data = getDictByJson("data1.json")
        logger.debug("Get request from IP {}.".format(request.remote_addr))
        return data
    else:
        return "Invalid request"

def startSocket():
    import socket

    # Define host and port
    HOST = '103.56.160.36'
    PORT = 12345

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}...")

    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break  # Break the loop if no data is received
        print(f"Received from client: {data}")

        # Echo the received data back to the client
        client_socket.sendall(data.encode('utf-8'))

    # Close the connection
    client_socket.close()

# startSocket()