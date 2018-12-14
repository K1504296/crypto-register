from coinmarketcap import Market

def getTRXUSD():
    coinmarket = Market()
    return coinmarket.ticker(1958)["data"]["quotes"]["USD"]["price"]