"""
This file contains the mean reversion strategy.
It will tell us when to buy and sell based on the Bollinger Bands indicator from indicators/bollinger.py.


"""

from ..indicators.bollinger import bollinger_bands

import pandas as pd



    
class MeanReversionStrategy:
    def __init__(self):
        self.position = None  # Can be "LONG", "SHORT", or None
        self.entry_price = None

    def bollinger_signal(price, sma, lower, upper):     
        if price < lower:
            return "BUY"
        elif price > upper:
            return "SELL"
        else:
            return "HOLD"

    
