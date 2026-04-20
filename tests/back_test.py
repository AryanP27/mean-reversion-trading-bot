from ..strategy.mean_reversion import MeanReversionStrategy

def test_buy_signal_when_price_below_lower_band():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    price = 90
    sma = 100
    lower = 95
    upper = 105
    volatility = upper - lower

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert decision.action == "BUY"
    assert decision.reason == "Price below lower Bollinger Band"

def test_sell_signal_when_price_above_upper_band():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    price = 120 
    sma = 100
    lower = 95
    upper = 105
    volatility = upper - lower

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert decision.action == "SELL"
    assert decision.reason == "Price above upper Bollinger Band"

def test_hold_signal_when_price_within_bands():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)
    
    price = 100 
    sma = 100
    lower = 95
    upper = 105
    volatility = upper - lower

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert decision.action == "HOLD"
    assert decision.reason == "No trade signal"

def test_volatility_too_high():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    price = 100 
    sma = 100
    lower = 95
    upper = 200
    volatility = upper - lower

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert decision.action == "HOLD"
    assert decision.reason == "High volatility"


def test_volatility_too_high():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    price = 100 
    sma = 100
    lower = 95
    upper = 96
    volatility = upper - lower

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert decision.action == "HOLD"
    assert decision.reason == "Low volatility"