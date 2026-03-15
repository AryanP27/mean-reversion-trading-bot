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
    def __init__(self, low_vol, high_vol, sizing_constant):
        self.position = None
        self.entry_price = None
        self.low_vol = low_vol
        self.high_vol = high_vol
        self.sizing_constant = sizing_constant

    # Gives Bollinger Band signal
    def bollinger_signal(self, price, sma, lower, upper):     
        if price < lower:
            return "BUY"
        elif price > upper:
            return "SELL"
        else:
            return "HOLD"
    
    # Used for decision making. Will take in stuff and then pass it to bot.py.
    def decision(self, price, sma, lower_band, upper_band, volatility):
        signal = self.bollinger_signal(price, sma, lower_band, upper_band)

        if volatility > self.high_vol:
            return Decision(
                action="Hold", 
                reason="High volatility", 
                timestamp=pd.Timestamp.now().timestamp(),
                size=0.0
            )
        if volatility < self.low_vol:
            return Decision(
                action="Hold", 
                reason="Low volatility", 
                timestamp=pd.Timestamp.now().timestamp(),
                size=0.0
            )
        
        size = self.sizing_constant / max(volatility, 1e-6)

        if signal == "BUY" and self.position != "LONG":
            self.position = "LONG"
            self.entry_price = price
            return Decision(
                action="BUY", 
                reason="Price below lower Bollinger Band", 
                timestamp=pd.Timestamp.now().timestamp(),
                size=size
            )
        if signal == "SELL" and self.position != "SHORT":
            self.position = "SHORT"
            self.entry_price = price
            return Decision(
                action="SELL", 
                reason="Price above upper Bollinger Band", 
                timestamp=pd.Timestamp.now().timestamp(),
                size=size
            )
        return Decision(
            action="HOLD", 
            reason="No trade signal", 
            timestamp=pd.Timestamp.now().timestamp(),
            size=0.0
        )