from binance.client import Client

def getTRXUSD(key, pwd):
    client = Client(key, pwd)
    ticker = client.get_symbol_ticker(symbol='TRXUSDT')
    return float(ticker["price"])