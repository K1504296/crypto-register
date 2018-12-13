import json

class Inventory:

    def __init__(self):
        with open('localdata/inventory.json', 'r') as myfile:
            self.items = json.loads(myfile.read())

inventory = Inventory()