

class User():
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address


user = User("", "", "")

def setUser(username, password, address):
    user.username = username
    user.password = password
    user.address = address