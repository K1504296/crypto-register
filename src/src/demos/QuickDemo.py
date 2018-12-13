'''

    Quick Demo for Class

        This allows you to get updates to your wallet and check your balance

'''
import sys
import time
import os
from TronAPI import *

def quickDemo():
    address = input("Please enter your public address  \n")

    cachedhashes = []

    balance = str(getbalance(address))

    if (balance != str(False)):
        print("Your current balance is : ", str(formatBalance(balance)), "TRX", "\n")
        print("Your most recent transactions are the following \n ")
        for transaction in gettransactionobjects(address):
            cachedhashes.append(transaction.hash)
            print(transaction)

    else :
        print("You have no balance in your account")

    while(1):
        time.sleep(2)

        newtransactions = gettransactionobjects(address)
        if (newtransactions):

            if (len(newtransactions) > len(cachedhashes)):
                pass

            else:
                lastTransaction = getlasttransactionobject(address)
                if (lastTransaction.hash not in cachedhashes):
                    print(lastTransaction)
                    cachedhashes.append(lastTransaction.hash)



