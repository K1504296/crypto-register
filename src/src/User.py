

class User():
    def __init__(self, username, password, address, binance=False, twilio=False):
        self.username = username
        self.password = password
        self.address = address
        self.binance = binance
        self.twilio = twilio


user = User("", "", "")


def setUser(username, password, address, binance=False, twilio=False):
    user.username = username
    user.password = password
    user.address = address
    user.binance = binance
    user.twilio = twilio