'''

    Transaction Object with information shown on Business Owner screen
        - Hash
        - From Address
        - To Address
        - Amount
        - Time stamp

'''

class Transaction:

    def __init__(self, hash, fromAddress, toAddress, amount, timestamp):
        self.hash        = hash
        self.fromAddress = fromAddress
        self.toAddress   = toAddress
        self.amount      = amount
        self.timestamp   = timestamp


    def __init__(self, transferdata):
        self.hash        = transferdata["transactionHash"]
        self.amount      = transferdata["amount"]
        self.timestamp   = transferdata["timestamp"]
        self.fromAddress = transferdata["transferFromAddress"]
        self.toAddress   = transferdata["transferToAddress"]


    def toStr(self):
        return "Hash   : " + self.hash + "\n" + \
               "From   : " + self.fromAddress + "\n" + \
               "Amount : " + str(self.amount) + "\n" + \
               "Time   : " + str(self.timestamp) + "\n"

    def fromStr(self):
        return "Hash   : " + self.hash + "\n" + \
               "To     : " + self.toAddress + "\n" + \
               "Amount : " + str(self.amount) + "\n" + \
               "Time   : " + str(self.timestamp) + "\n"


    def __str__(self):
        return "Hash   : " + self.hash + "\n" + \
               "From   : " + self.fromAddress + "\n" + \
               "To     : " + self.toAddress + "\n" + \
               "Amount : " + str(self.amount) + "\n" + \
               "Time   : " + str(self.timestamp) + "\n"

    def __eq__(self, other):
        if (isinstance(other, Transaction)):
            return self.hash == other.hash
        return NotImplemented