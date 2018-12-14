import sys
import os
sys.path.append(os.getcwd() + "/../src")
from User import user

import CoinMarketCap
import Binance

def getTRXtoUSD():
    if (user.binance):
        Binance.getTRXUSD(user.binance[0], user.binance[1])
    return CoinMarketCap.getTRXUSD()

def USDtoTRX(USD):
    if (user.binance):
        return USD/Binance.getTRXUSD(user.binance[0], user.binance[1])
    return USD/CoinMarketCap.getTRXUSD()