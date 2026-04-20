import ccxt

class KrakenClient:
    def __init__(self):
        self.exchange = ccxt.kraken()

    def get_price(self, symbol="ETH/USD"):
        ticker = self.exchange.fetch_ticker(symbol)
        return ticker["last"]
