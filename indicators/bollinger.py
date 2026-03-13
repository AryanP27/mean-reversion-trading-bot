""" 
This file contains the Bollinger Bands indicator. 





"""

import pandas as pd

def bollinger_bands(prices, window=20):
    variance = prices.rolling(window).var()
    sma = prices.rolling(window).mean()
    std = variance ** 0.5
    lower_band = sma - (2 * std)
    upper_band = sma + (2 * std)
    return sma, lower_band, upper_band


prices = pd.Series(range(1, 101))  # Place holder price data. Will be removed soon. 
sma, lower_band, upper_band = bollinger_bands(prices)
print("SMA:\n", sma.tail())
print("Lower Band:\n", lower_band.tail())
print("Upper Band:\n", upper_band.tail())

