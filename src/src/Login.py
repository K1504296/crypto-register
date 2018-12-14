import json
import os
from User import *

def login(username, password):
    data = searchfile("localdata/users.json", username, password)
    if len(data) > 0:
        binance = False
        twilio = False
        if "twilio"  in data.keys():
            twilio = [data[username]["twilio"]["key"], data[username]["twilio"]["pwd"], data[username]["twilio"]["phone"], data[username]["twilio"]["twphone"]]
        if "binance"  in data.keys():
            binance = [data[username]["binance"]["key"], data[username]["binance"]["pwd"]]
        setUser(username, password, data["address"], binance, twilio)
        return True
    else:
        return False

def searchfile(file, username, password):
    '''

    :param file:
    :return:
    '''

    with open(file) as file:
        data = json.loads(file.read())
    if ((username in data.keys()) and (data[username]["password"] == password)):
        return data[username]
    return {}

def register(username, password, address, binance=False, twilio=False):
    data = {}
    if os.stat("localdata/users.json").st_size != 0:
        with open("localdata/users.json") as file:
            data = json.loads(file.read())
    data[username] = {}
    data[username]['password'] = password
    data[username]['address']  = address

    if (twilio):
        data[username]["twilio"] = {
            'key': twilio[0],
            'pwd': twilio[1],
            'phone' : twilio[2],
            'twphone': twilio[3]
        }

    if (binance):
        data[username]["binance"] = {
            'key': binance[0],
            'pwd': binance[1],
        }

    with open("localdata/users.json", 'w') as outfile:
        json.dump(data, outfile)