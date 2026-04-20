"""
This file contains the main bot class that will tie everything together.
It will use the mean reversion strategy from strategy/mean_reversion.py and the Bollinger Bands indicator 
from indicators/bollinger.py to make trading decisions.

"""


import time
from collections import deque

from ..strategy.mean_reversion import MeanReversionStrategy
from ..indicators.bollinger import bollinger_bands
from ..exchange.exchange_client import KrakenClient


class TradingBot:
    def __init__(self, strategy, exchange, window=20):
        self.strategy = strategy
        self.exchange = exchange
        self.window = window

        self.prices = deque(maxlen=window)

    def run_step(self, symbol="ETH/USD"):
        price = self.exchange.get_price(symbol)
        self.prices.append(price)

        if len(self.prices) < self.window:
            print(f"Waiting for {self.window - len(self.prices)} more prices...")
            return None

        sma, upper, lower = bollinger_bands(list(self.prices))

        volatility = upper - lower

        decision = self.strategy.decision(price, sma, lower, upper, volatility)

        print(decision)
        return decision


def run_realtime_bot():
    exchange = KrakenClient()

    strategy = MeanReversionStrategy(
        low_vol=5,
        high_vol=50,
        sizing_constant=1.0
    )

    bot = TradingBot(strategy, exchange, window=20)

    symbol = "ETH/USD"

    print("Starting real-time trading bot...")

    while True:
        bot.run_step(symbol)
        time.sleep(15)