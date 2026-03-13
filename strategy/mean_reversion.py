"""
This file contains the mean reversion strategy.
It will tell us when to buy and sell based on the Bollinger Bands indicator from indicators/bollinger.py.


"""

from trading_bot.indicators.bollinger import bollinger_bands

import pandas as pd

def bollinger_signal(price, sma, upper, lower):

    prices = pd.Series(range(1, 101))  # Place holder price data. Will be removed soon. 
    sma, lower_band, upper_band = bollinger_bands(prices)
    latest_sma = sma.iloc[-1]
    latest_lower = lower_band.iloc[-1]
    latest_upper = upper_band.iloc[-1]
    latest_price = prices.iloc[-1]

    if price < lower:
        return "BUY"
    elif price > upper:
        return "SELL"
    else:
        return "HOLD"
    
