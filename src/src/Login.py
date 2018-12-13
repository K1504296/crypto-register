import json
import os
from User import *

def login(username, password):
    data = searchfile("localdata/users.json", username, password)
    if len(data) > 0:
        setUser(username, password, data["address"])
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
    if ((username in data.keys()) and (data[username][0]["password"] == password)):
        return data[username][0]
    return {}

def register(username, password, address):
    data = {}
    if os.stat("localdata/users.json").st_size != 0:
        with open("localdata/users.json") as file:
            data = json.loads(file.read())
    data[username] = []
    data[username].append({
        'password': password,
        'address': address,
    })

    with open("localdata/users.json", 'w') as outfile:
        json.dump(data, outfile)