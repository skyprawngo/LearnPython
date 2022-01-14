# VBS - Volatility Breakthrough Strategy. 변동성 돌파 전략 구현하기
import os
import schedule
import datetime
import getpass
import ccxt

binance = ccxt.binance()

class Volatility_BS(object):
    def __init__(
        self,
        ask,
        open_now,
        high_past,
        low_past,
        
        k = 0.5,
    ):
        super().__init__()
        self.ask = int(ask)
        self.open_now = int(open_now)
        self.high_past = int(high_past)
        self.low_past = int(low_past)
        
        self.right_side = self.open_now + (self.high_past - self.low_past)*k
        
    def VBS_calc(self):
        if self.ask > self.right_side:
            return True
        else: return False
        
class ccxt_dataIO:
    def __init__(
        self,
    ):
        pass
    def get_account(self):
        global binance
        account_path = os.path.normpath(os.path.join(os.path.abspath(__file__),"account.txt"))
        with open(account_path) as f:
            lines = f.readlines()
            api_key = lines[0].strip() 
            secret = lines[1].strip() 
        binance = ccxt.binance(config={
            'apiKey': api_key,
            'secret': secret
        })
        print(api_key)
        print(secret)

if __name__ == "__main__":
    ccxt_dataIO.get_account()
    pass