import sys
import os
sys.path.append(os.getcwd() + "/../img")
from Login import register, login
from PyQt4 import QtGui, QtCore
from App import MainWidget
from Style import *
from TronAPI import *

LOGIN_WINDOW_SIZE = 300
MAIN_WINDOW_SIZE = 1000

class LoginWindow(QtGui.QMainWindow):
    def __init__(self, app, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.app = app
        self.setStyleSheet(DBKG)
        self.setGeometry(0, 0, LOGIN_WINDOW_SIZE + 500, LOGIN_WINDOW_SIZE)
        self.setCentralWidget(LoginWidget(self))

    def movetoRegister(self):
        self.setCentralWidget(RegisterWidget(self))

    def backtoLogin(self):
        self.setCentralWidget(LoginWidget(self))

    def closeLogin(self):
        self.setGeometry(0, 0, MAIN_WINDOW_SIZE + 500, MAIN_WINDOW_SIZE)
        self.setCentralWidget(MainWidget(self))


class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        self.setStyleSheet(LBKG)
        LoginGrid(self)

    def movetoRegister(self):
        self.parent().movetoRegister()

    def closeLogin(self):
        self.parent().closeLogin()

class LoginGrid(QtGui.QGridLayout):
    def __init__(self, parent=None):
        super(LoginGrid, self).__init__(parent)

        self.username = QtGui.QLineEdit("Username")
        self.username.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.password = QtGui.QLineEdit("Password")
        self.password.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.submit = QtGui.QPushButton("Login")
        self.submit.clicked.connect(self.loginUser)
        self.submit.setStyleSheet("color: rgb(255, 255, 255); " + NO_BORDER)

        self.register = QtGui.QPushButton("Register")
        self.register.clicked.connect(self.movetoRegister)
        self.register.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.forgot = QtGui.QPushButton("Forgot Password")
        self.forgot.setStyleSheet("color: rgb(255, 255, 255);"+ NO_BORDER)

        self.addWidget(self.username, 0, 0, 1, 2)
        self.addWidget(self.password, 1, 0, 1, 2)
        self.addWidget(self.submit, 2, 0, 1, 2)
        self.addWidget(self.register, 3, 0, 1, 1)
        self.addWidget(self.forgot, 3, 1, 1, 1)

    def movetoRegister(self):
        self.parent().movetoRegister()

    def loginUser(self):
        if login(self.username.text(), self.password.text()):
            self.parent().closeLogin()
        else:
            print("Failure")

class RegisterWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RegisterWidget, self).__init__(parent)
        self.setStyleSheet("background-color:#1C2833;")
        RegisterGrid(self)

    def backtoLogin(self):
        self.parent().backtoLogin()

class RegisterGrid(QtGui.QGridLayout):
    def __init__(self, parent=None):
        super(RegisterGrid, self).__init__(parent)

        self.username = QtGui.QLineEdit("Username")
        self.username.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.password = QtGui.QLineEdit("Password")
        self.password.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.address = QtGui.QLineEdit("TRON Public Address")
        self.address.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.optional = QtGui.QLabel("Optional")

        self.binancekeystr = "Binance API Key"
        self.binancekey = QtGui.QLineEdit("Binance API Key")
        self.binancekey.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.binancepwdstr = "Binance API Password"
        self.binancepwd = QtGui.QLineEdit("Binance API Password")
        self.binancepwd.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.twiliokeystr = "Twilio API Key"
        self.twiliokey = QtGui.QLineEdit("Twilio API Key")
        self.twiliokey.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.twiliopwdstr = "Twilio API Password"
        self.twiliopwd = QtGui.QLineEdit("Twilio API Password")
        self.twiliopwd.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.twphonenumber = QtGui.QLineEdit("Twilio PhoneNumber")
        self.twphonenumber.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.phonenumber = QtGui.QLineEdit("PhoneNumber")
        self.phonenumber.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.register = QtGui.QPushButton("Register")
        self.register.clicked.connect(self.registerUser)
        self.register.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.login = QtGui.QPushButton("Back to Login")
        self.login.clicked.connect(self.backtoLogin)
        self.login.setStyleSheet("color: rgb(255, 255, 255);" + NO_BORDER)

        self.addWidget(self.username, 0, 0, 1, 2)
        self.addWidget(self.password, 1, 0, 1, 2)
        self.addWidget(self.address, 2, 0, 1, 2)
        self.addWidget(self.optional, 3, 0, 1, 2)
        self.addWidget(self.binancekey, 4, 0, 1, 1)
        self.addWidget(self.binancepwd, 4, 1, 1, 1)
        self.addWidget(self.twiliokey, 5, 0, 1, 1)
        self.addWidget(self.twiliopwd, 5, 1, 1, 1)
        self.addWidget(self.phonenumber, 6, 0, 1, 2)
        self.addWidget(self.register, 7, 0, 1, 1)
        self.addWidget(self.login, 7, 1, 1, 1)

    def backtoLogin(self):
        self.parent().backtoLogin()


    def registerUser(self):
        if (validAddress(self.address.text())):
            twilio = False
            binance = False
            if (self.twiliopwd.text() != self.twiliopwdstr and self.twiliokey.text() != self.twiliokeystr):
                twilio = [self.twiliokey.text(), self.twiliopwd.text(), self.phonenumber.text(), self.twphonenumber.text()]

            if (self.binancepwd.text() != self.binancepwdstr and self.binancekey.text() != self.binancekeystr):
                binance = [self.binancekey.text(), self.binancepwd.text()]
            register(self.username.text(), self.password.text(), self.address.text(), binance, twilio)
            self.backtoLogin()


def runLoginApp():
    app = QtGui.QApplication(sys.argv)
    w = LoginWindow(app)
    w.show()
    sys.exit(app.exec_())
