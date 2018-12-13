from binance.client import Client


api_key = "MUFGesWsqo2Bdcz0wV6RnVJPWIDnhhzaNMgC80PngVbsjcJnVQOFpXplXFf7Btix"
api_secret = "8Noea8P56FWbdOPLX1GjmTBUV7S6llFq5YpsKO0WsY0UWvW8P7P3BqA3hqm9eKpH"
client = Client(api_key, api_secret)

def getTRXtoUSD():
    ticker = client.get_symbol_ticker(symbol='TRXUSDT')
    return float(ticker["price"])

def USDtoTRX(USD):
    return USD/getTRXtoUSD()