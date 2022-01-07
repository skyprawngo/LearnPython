import os
import pandas as pd
import ccxt

class CCXT_Binance(object):
    binance = ccxt.binance()
    api_key = None
    secret = None
    
    def __init__(self):
        # self.enroll_account_txt()
        pass
        
    def enroll_account_ui(self, api_key, secret):
        self.binance = ccxt.binance(config={
            'apiKey': api_key,
            'secret': secret
        })
        
    def enroll_account_txt(self):
        try:
            account_path = os.path.normpath(os.path.join(os.getcwd(),"ccxt_learn/account.txt"))
            with open(account_path) as reader:
                lines = reader.readlines()
                api_key = lines[0].strip() 
                secret = lines[1].strip()
            self.binance = ccxt.binance(config={
                'apiKey': api_key,
                'secret': secret
            })
        except:
            print("acount.txt 파일에 apikey가 저장되어있지 않습니다!")
            self.enroll_account_ui()
    
    def save_account_ui2txt(self):
        pass
    
    def load_markets(self):
        markets= self.binance.load_markets()
        return markets
    
    def fetch_ticker(self, coin_name):
        btc = self.binance.fetch_ticker(coin_name)
        return btc
    
    def fetch_ohlcv(
        self, 
        coin_name, 
        timeframe = "1m", 
        since = None, 
        limit = None, 
        params = {}
    ):
        btc_ohlcv = self.binance.fetch_ohlcv(
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
        balance = self.binance.fetch_balance()
        return balance


if __name__ == "__main__":
    a = CCXT_Binance().fetch_ticker("BTC/BUSD")
    print(a)
    print(a["close"])
    print(a["open"])
    print(a["last"])