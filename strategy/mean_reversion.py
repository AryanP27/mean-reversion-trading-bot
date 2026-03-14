"""
This file contains the mean reversion strategy.
It will tell us when to buy and sell based on the Bollinger Bands indicator from indicators/bollinger.py.


"""

from ..indicators.bollinger import bollinger_bands

import pandas as pd
from dataclasses import dataclass

@dataclass
class Decision:
    action: str
    reason: str
    timestamp: float
    size: float = 0.0
    
class MeanReversionStrategy:
    def __init__(self):
        self.position = None
        self.entry_price = None

    def bollinger_signal(self, price, sma, lower, upper):     
        if price < lower:
            return "BUY"
        elif price > upper:
            return "SELL"
        else:
            return "HOLD"
    
    def decision(self, price, sma, lower_band, upper_band, volatility):

        pass
