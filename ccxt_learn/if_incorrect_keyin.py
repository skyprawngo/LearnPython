import ccxt

binance = ccxt.binance(config={
    'apiKey': "asdasd",
    'secret': "asdasd"
})

binance.fetch_balance()