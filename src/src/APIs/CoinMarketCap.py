from coinmarketcap import Market

def getTRXtoUSD():
    coinmarket = Market()
    return coinmarket.ticker(1958)["data"]["quotes"]["USD"]["price"]