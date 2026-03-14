"""
This file contains the main bot class that will tie everything together.
It will use the mean reversion strategy from strategy/mean_reversion.py and the Bollinger Bands indicator from indicators/bollinger.py to make trading decisions.

"""

from ..strategy.mean_reversion import MeanReversionStrategy

class TradingBot:
    def __init__(self):
        self.strategy = MeanReversionStrategy()
    
    def run(self, price, sma, lower_band, upper_band):
        # This method will be called to run the bot with new price data.
        # It will use the strategy to make trading decisions based on the price data and indicators.
        pass