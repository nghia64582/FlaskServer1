from flask import Flask
from flask import request
import json
import time
from datetime import datetime as dt
from logger import Logger
import traceback
import random as rd
from config import *

print(1)
app = Flask(__name__)
print(2)
logger = Logger()
print(3)
logger.debug("Server start at {}".format(dt.now().strftime("%H:%M:%S")))
print(4)
app.run(debug = True)
print(5)
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
