from Bill import *
from QuickDemo import *


def transactionDemo():
    bill = Bill()
    val = input("Enter Items and quantities with a space between \n For example: Apple 2 \n Or Enter finish to find the total\n")
    while(1):

        if (val == "finish"):
            print("The entire bill is the following : ")
            bill.printBill()

        splitval = val.split()
        if (len(splitval) == 2):
            bill.add(splitval[0], int(splitval[1]))

        val = input()

def fullDemo():
    val = input("Please enter one of the following options : wallet, maketransaction\n")

    if (val == "wallet"):
        quickDemo()
    elif (val == "maketransaction"):
        transactionDemo()
