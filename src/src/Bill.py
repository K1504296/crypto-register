'''

    Bill

'''
from Item import *
from CoinMarketCap import *

class Bill:

    def __init__(self):
        self.items = {}
        self.sum = 0

    def add(self, name, quantity):
        # If item already exists in the bill
        if (name in self.items.keys()):
            self.items[name].add(quantity)
        # If it is a new item
        else :
            self.items[name] = Item(name, quantity)
        self.sum += float(quantity)*float(self.items[name].price)

    def printBill(self):
        print(self.toString())

    def trxTotal(self):
        return bill.sum/getTRXtoUSD()

    def toString(self):
        billstring = ""
        for item in self.items:
            name = self.items[item].name
            length = len(name)
            billstring += name +  " "*(20-length) +  str(self.items[item].quantity) + " "*3 +  "x" + " "*3 +  str(self.items[item].price) + "\n"

        return billstring


    def clearbill(self):
        self.items = {}
        self.sum = 0

bill = Bill()