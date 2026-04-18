# mean-reversion-trading-bot
```
## Data Flow

[MARKET / EXCHANGE]
        |
        v
[exchange_client.py]        <- gets raw API data, submits orders
        |
        v
      [bot.py]  <----------- [config.py]  [logger.py]
        |
        v
   [bollinger.py]            <- calculates rolling mean, upper/lower bands
        |
        v
[mean_reversion.py]         <- actual strategy
        |
        |
        v
      [bot.py]               <- executes order via exchange_client.py
        |
        v
[MARKET / EXCHANGE]


--- Supporting modules ---

config.py   — params, thresholds, symbol, timeframe
logger.py   — trades, signals, errors → file/stdout

--- Tests (mock inputs) ---

test_indicators.py  — unit tests bollinger.py in isolation
test_strategy.py    — unit tests mean_reversion.py in isolation
```
