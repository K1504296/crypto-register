import requests
from Transaction import *
from bitcoin.base58 import *

gridendpoint      = 'https://api.trongrid.io'
scanendpoint      = 'https://api.tronscan.org'
solidity_node     = 'walletsolidity'
solidity_node_ext = 'walletextension'
full_node         = 'wallet'
api               = 'api'


def validresponse(response):
    '''
    Check if the response is a valid response
    :param response:
    :return:
    '''
    if (len(response.json())):
        return True
    return False


def validAddress(address):
    response = requests.get(scanendpoint + '/' + api + '/' + "account", params = {"address" : address})
    if response.json()["total"] == 1:
        return True
    return False


def getbalance(address):
    '''

        Get the balance of an address

    :param address:
    :return:
    '''
    hexstring = base58tohexstring(address)
    response = requests.get(gridendpoint + '/' + solidity_node + '/' +
                            "getaccount", params = {"address" : hexstring})
    if (validresponse(response)):
        return response.json()["balance"]
    return False


def gettransactions(address):
    '''

        GetTransaction API

    :param address:
    :return:

            A list of transfers (dictionaries) with the following info:

            {
              "hash": "string",
              "block": 0,
              "timestamp": "2018-11-13T20:48:28.782Z",
              "confirmed": true,
              "ownerAddress": "string",
              "toAddress": "string",
              "contractData": {
                "boolean": true,
                "number": true,
                "string": true,
                "object": true,
                "array": true,
                "null": true
              },
              "contractType": 0,
              "data": "string"
            }
    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transaction", params = {"address" : address})
    if (response):
        return response.json()["data"]
    return False

def gettransfers(address):
    '''
    GetTransfer API

    :param address: The public address
    :return:

            A list of transfers (dictionaries) with the following info:

            {
              "id": "string",
              "transactionHash": "string",
              "block": 0,
              "timestamp": "2018-11-13T22:22:34.141Z",
              "transferFromAddress": "string",
              "transferToAddress": "string",
              "amount": 0,
              "tokenName": "string",
              "confirmed": true
            }
    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"address" : address})
    if (response):
        return response.json()["data"]
    return False

def gettransfersto(address):
    '''
    GetTransfer API

    :param address: The public address
    :return:

            A list of transfers (dictionaries) with the following info:

            {
              "id": "string",
              "transactionHash": "string",
              "block": 0,
              "timestamp": "2018-11-13T22:22:34.141Z",
              "transferFromAddress": "string",
              "transferToAddress": "string",
              "amount": 0,
              "tokenName": "string",
              "confirmed": true
            }
    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"to" : address})
    if (response):
        return response.json()["data"]
    return False

def gettransfersfrom(address):
    '''
    GetTransfer API

    :param address: The public address
    :return:

            A list of transfers (dictionaries) with the following info:

            {
              "id": "string",
              "transactionHash": "string",
              "block": 0,
              "timestamp": "2018-11-13T22:22:34.141Z",
              "transferFromAddress": "string",
              "transferToAddress": "string",
              "amount": 0,
              "tokenName": "string",
              "confirmed": true
            }
    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"from" : address})
    if (response):
        return response.json()["data"]
    return False


def getlasttransfer(address):
    '''

    :param address:
    :return:

        A dictionary of info about the latest transfer

    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"address" : address})
    if (response):
        responsedata = response.json()["data"]
        max = responsedata[0]["timestamp"];
        lasttransfer = responsedata[0]
        for transfer in responsedata:
            if (transfer["timestamp"] > max):
                max = transfer["timestamp"]
                lasttransfer = transfer
        return lasttransfer
    return False

def getlasttransferto(address):
    '''

    :param address:
    :return:

        A dictionary of info about the latest transfer

    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"to" : address})
    if (response):
        responsedata = response.json()["data"]
        max = responsedata[0]["timestamp"];
        lasttransfer = responsedata[0]
        for transfer in responsedata:
            if (transfer["timestamp"] > max):
                max = transfer["timestamp"]
                lasttransfer = transfer
        return lasttransfer
    return False

def getlasttransferfrom(address):
    '''

    :param address:
    :return:

        A dictionary of info about the latest transfer

    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"from" : address})
    if (response):
        responsedata = response.json()["data"]
        max = responsedata[0]["timestamp"];
        lasttransfer = responsedata[0]
        for transfer in responsedata:
            if (transfer["timestamp"] > max):
                max = transfer["timestamp"]
                lasttransfer = transfer
        return lasttransfer
    return False

def getlasttransactionobject(address):
    '''

    :param address:
    :return:

        A Transaction object with info about the latest transfer

    '''
    transferdata = getlasttransfer(address)
    if (transferdata):
        return Transaction(transferdata)
    return False

def getlasttransactionobjectto(address):
    '''

    :param address:
    :return:

        A Transaction object with info about the latest transfer

    '''
    transferdata = getlasttransferto(address)
    if (transferdata):
        return Transaction(transferdata)
    return False

def getlasttransactionobjectfrom(address):
    '''

    :param address:
    :return:

        A Transaction object with info about the latest transfer

    '''
    transferdata = getlasttransferfrom(address)
    if (transferdata):
        return Transaction(transferdata)
    return False


def gettransactionobjects(address):
    '''

    :param address:
    :return:

        A list of Transaction objects for all transactions

    '''
    transactions = []
    rawtransfers = gettransfers(address)

    if (rawtransfers):
        for transaction in rawtransfers:
            transactions.append(Transaction(transaction))
    return transactions


def gettransactionobjectsto(address):
    '''

    :param address:
    :return:

        A list of Transaction objects for all transactions

    '''
    transactions = []
    rawtransfers = gettransfersto(address)

    if (rawtransfers):
        for transaction in rawtransfers:
            transactions.append(Transaction(transaction))
    return transactions

def gettransactionobjectsfrom(address):
    '''

    :param address:
    :return:

        A list of Transaction objects for all transactions

    '''
    transactions = []
    rawtransfers = gettransfersfrom(address)

    if (rawtransfers):
        for transaction in rawtransfers:
            transactions.append(Transaction(transaction))
    return transactions


def printtransfers(address):
    '''

    :param address:
    :return:

        Print all the current Transfer objects

    '''
    for transfer in gettransfers(address):
        print(Transaction(transfer))


def getformattedBalance(address):
    return formatBalance(getbalance(address))

def formatBalance(balance):
    '''
        Convert API balance term to a traditional version

    :param balance:
            An integer with all 6 digits after decimal

    :return:

            A formatted number that looks like : 45.34
    '''
    return float(str(balance)[:-4])/100


def base58tohexstring(address):
    '''

    :param address:
    :return:
    '''
    return decode(address).hex()[:-8]