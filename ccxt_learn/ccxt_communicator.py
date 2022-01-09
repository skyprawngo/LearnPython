import os
import pandas as pd
import ccxt
import getpass
import pickle

class CCXT_Binance(object):
    binance = ccxt.binance()
    api_key = None
    secret = None
    
    def __init__(self):
        # self.enroll_account_txt()
        pass
        
    def enroll_account_ui(api_key, secret):
        CCXT_Binance.binance = ccxt.binance(config={
            'apiKey': api_key,
            'secret': secret
        })
        
    def enroll_account_txt():
        username = getpass.getuser()
        account_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist/user_data.txt"))
        with open(account_path, "rb") as reader:
            data = pickle.load(reader)
            key = [data["apikey"], data["secretkey"]]
        CCXT_Binance.binance = ccxt.binance(config={
            'apiKey': key[0],
            'secret': key[1]
        })
    
    def load_markets():
        markets= CCXT_Binance.binance.load_markets()
        return markets
    
    def fetch_ticker(coin_name):
        btc = CCXT_Binance.binance.fetch_ticker(coin_name)
        return btc
    
    def fetch_ohlcv(
        coin_name, 
        timeframe = "1m", 
        since = None, 
        limit = None, 
        params = {}
    ):
        btc_ohlcv = CCXT_Binance.binance.fetch_ohlcv(
            symbol = coin_name,
            timeframe = timeframe,
            since = since,
            limit = limit,
            params = params
        )
        # print(pd.DataFrame(btc_ohlcv))
        df = pd.DataFrame(btc_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df_datetime = pd.to_datetime(df['timestamp'], unit='ms')
        df.insert(0,"datetime", df_datetime, True)
        # df.set_index('datetime', inplace=True)
        return df
    
    def fetch_balance(self):
        balance = CCXT_Binance.binance.fetch_balance()
        return balance


if __name__ == "__main__":
    a = CCXT_Binance().fetch_ticker("BTC/BUSD")
    print(a)
    print(a["close"])
    print(a["open"])
    print(a["last"])
    CCXT_Binance().enroll_account_txt()