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

def test_volatility_too_low():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    price = 100 
    sma = 100
    lower = 95
    upper = 96
    volatility = upper - lower

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert decision.action == "HOLD"
    assert decision.reason == "Low volatility"

def test_position_updates_on_buy():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    price = 90
    sma = 100
    lower = 95
    upper = 105
    volatility = upper - lower  # = 10 (normal)

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert strategy.position == "LONG"
    assert decision.action == "BUY"

def test_position_updates_on_sell():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    price = 120
    sma = 100
    lower = 95
    upper = 105
    volatility = upper - lower  # = 10 (normal)

    decision = strategy.decision(price, sma, lower, upper, volatility)

    assert strategy.position == "SHORT"
    assert decision.action == "SELL"

def test_no_duplicate_buy_when_already_long():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    # First BUY
    strategy.decision(price=90, sma=100, lower_band=95, upper_band=105, volatility=10)
    assert strategy.position == "LONG"

    # Second BUY attempt
    decision = strategy.decision(price=80, sma=100, lower_band=95, upper_band=105, volatility=10)

    assert decision.action == "HOLD"
    assert decision.reason == "No trade signal"
    assert strategy.position == "LONG"

def test_no_duplicate_sell_when_already_short():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    # First SELL
    strategy.decision(price=120, sma=100, lower_band=95, upper_band=105, volatility=10)
    assert strategy.position == "SHORT"

    # Second SELL attempt
    decision = strategy.decision(price=130, sma=100, lower_band=95, upper_band=105, volatility=10)

    assert decision.action == "HOLD"
    assert decision.reason == "No trade signal"
    assert strategy.position == "SHORT"

def test_decision_object_structure():
    strategy = MeanReversionStrategy(low_vol=5, high_vol=50, sizing_constant=1.0)

    decision = strategy.decision(price=90, sma=100, lower_band=95, upper_band=105, volatility=10)

    assert hasattr(decision, "action")
    assert hasattr(decision, "reason")
    assert hasattr(decision, "timestamp")
    assert hasattr(decision, "size")
