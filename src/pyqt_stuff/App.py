import sys
import os
sys.path.append(os.getcwd() + "/../src")
from PyQt4 import QtGui, QtCore
from User import user
from CoinMarketCap import *
from TronAPI import *
from Inventory import *
from Bill import bill
from Printer import *


class ToAddressList(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(ToAddressList, self).__init__(parent)
        self.cachedhashes = []

        for transaction in gettransactionobjectsto(user.address):
            self.cachedhashes.append(transaction.hash)
            self.addItem(transaction.toStr())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateToTransactions)
        self.timer.start(5000)

    def updateToTransactions(self):
        newtransactions = gettransactionobjectsto(user.address)

        if (len(newtransactions) > len(self.cachedhashes)):
            pass
        else:
            lastTransaction = getlasttransactionobjectto(user.address)
            if (lastTransaction.hash not in self.cachedhashes):
                QtGui.QMessageBox.information(QtGui.QWidget(),  "Transaction Successful", "Recieved $" + str(formatBalance(lastTransaction.amount)) +  " from " + lastTransaction.toAddress)
                self.cachedhashes.append(lastTransaction.hash)
                self.addItem(lastTransaction.toStr())

class FromAddressList(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(FromAddressList, self).__init__(parent)
        self.cachedhashes = []

        for transaction in gettransactionobjectsfrom(user.address):
            self.cachedhashes.append(transaction.hash)
            self.addItem(transaction.fromStr())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateFromTransactions)
        self.timer.start(5000)

    def updateFromTransactions(self):
        newtransactions = gettransactionobjectsfrom(user.address)

        if (len(newtransactions) > len(self.cachedhashes)):
            pass
        else:
            lastTransaction = getlasttransactionobjectfrom(user.address)
            if (lastTransaction.hash not in self.cachedhashes):
                QtGui.QMessageBox.information(QtGui.QWidget(), "Transaction Successful", "Sent $" + str(formatBalance(lastTransaction.amount)) +  " to " + lastTransaction.toAddress)
                self.cachedhashes.append(lastTransaction.hash)
                self.addItem(lastTransaction.toStr())

class InventoryList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(InventoryList, self).__init__(parent)
        self.setStyleSheet("""QListWidget{background:rgb(130, 224, 170);}""")
        self.chosenItem = "DummyItem"

        self.list = QtGui.QListWidget(self)
        self.list.itemClicked.connect(self.choose)
        self.fillInventory()

        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.list)

    def choose(self, item):
        self.chosenItem = item.text()

    def fillInventory(self):
        for item in inventory.items:
            self.list.addItem(item)


class TransGrid(QtGui.QGridLayout):
    def __init__(self, parent=None):
        super(TransGrid, self).__init__(parent)
        self.setSpacing(50)
        self.list = InventoryList()

        self.quantity = QtGui.QLineEdit()

        self.addItemButton = QtGui.QPushButton("Add Item")
        self.addItemButton.clicked.connect(self.addProduct)

        self.finishTransaction = QtGui.QPushButton("Finish Transaction")
        self.finishTransaction.clicked.connect(self.finishtransaction)

        self.tally = QtGui.QListWidget()

        self.sum = QtGui.QLabel("")

        self.tally.setStyleSheet("""QListWidget{background:rgb(130, 224, 170);}""")
        self.quantity.setStyleSheet("""QLineEdit{background:rgb(22, 160, 133);}""")
        self.sum.setStyleSheet("""QLabel{background:rgb(22, 160, 133);}""")
        self.addItemButton.setStyleSheet("""QPushButton{background:rgb(133, 193, 233);}""")
        self.finishTransaction.setStyleSheet("""QPushButton{background:rgb(133, 193, 233);}""")

        self.addWidget(self.list, 0, 0, 3, 1)
        self.addWidget(self.quantity, 3, 0, 1, 1)
        self.addWidget(self.addItemButton, 4, 0, 1, 1)
        self.addWidget(self.finishTransaction, 4, 1, 1, 1)
        self.addWidget(self.tally, 0, 1, 3, 1)
        self.addWidget(self.sum, 3, 1, 1, 3)


    def addProduct(self):
        bill.add(self.list.chosenItem, int(self.quantity.text()))
        bill.printBill()
        self.sum.setText(str(bill.sum))
        self.tally.addItem(self.list.chosenItem + " "*5 + self.quantity.text() + "  x  " + inventory.items[self.list.chosenItem])

    def finishtransaction(self):
        self.tally.clear()
        self.sum.clear()
        self.quantity.clear()
        printOutFinalBill()
        bill.clearbill()

class WalletGrid(QtGui.QGridLayout):
    def __init__(self, parent=None):
        super(WalletGrid, self).__init__(parent)

        self.address = QtGui.QLabel(user.address)

        self.balance = QtGui.QLabel("")
        self.power = QtGui.QLabel("")
        self.exchange = QtGui.QLabel("")

        self.toBox = ToAddressList()
        self.fromBox = FromAddressList()

        self.addWidget(self.address, 0, 0, 1, 6)
        self.addWidget(self.balance, 1, 0, 1, 2)
        self.addWidget(self.power, 1, 2, 1, 2)
        self.addWidget(self.exchange, 1, 4, 1, 2)
        self.addWidget(self.toBox, 2, 0, 3, 3)
        self.addWidget(self.fromBox, 2, 3, 3, 3)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateWallet)
        self.timer.start(1000)

        self.setSpacing(30)

        self.address.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(130, 224, 170))

        self.balance.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(22, 160, 133))
        self.power.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(22, 160, 133))
        self.exchange.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(22, 160, 133))

        self.toBox.setStyleSheet("""QListWidget{background:rgb(133, 193, 233);}""")
        self.fromBox.setStyleSheet("""QListWidget{background:rgb(133, 193, 233);}""")

    def updateWallet(self):
        self.balance.setText(str(getformattedBalance(user.address)))
        self.exchange.setText(str(getTRXtoUSD()))


class MainWidget(QtGui.QTabWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setStyleSheet("background-color:#313131;")

        self.setTabPosition(2)

        self.walletwidget = QtGui.QWidget()
        self.walletwidget.setStyleSheet("background-color: (44, 62, 80)")
        self.transwidget = QtGui.QWidget()

        WalletGrid(self.walletwidget)
        TransGrid(self.transwidget)


        self.addTab(self.transwidget, "Transaction")
        self.addTab(self.walletwidget, "Wallet")
        self.show()
