
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import json
import time

app = Flask(__name__)

def saveDictToJsonFile(data, jsonFile):
    with open(jsonFile, 'w') as outfile:
        json.dump(data, outfile, indent = 4)

def getDictByJson(jsonFile):
    return json.load(open(jsonFile))


@app.route("/", methods = ["GET", "POST"])
def hello_world():
    try:
        if request.json != None:
            print("Request with json {}".format(request.json))
            if request.json.get("num") != None:
                num = int(request.json.get("num"))
                data = {"a": [i for i in range(num)]}
                saveDictToJsonFile(data, "data1.json")
                print("num : {}".format(num))
                return "Create json with size {}".format(num)
            else:
                return "Json do not have key <num>"
        else:
            print("Json is required.")
            return "Json is required."

    except:
        try:
            data = getDictByJson("data1.json")
            print("Data {}".format(data))
            return data
        except:
            print("Print time")
            return "Ver 1.2. Current time is {}".format(time.time())