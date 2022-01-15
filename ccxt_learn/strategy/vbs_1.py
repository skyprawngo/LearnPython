# VBS - Volatility Breakthrough Strategy. 변동성 돌파 전략 구현하기
import os
import schedule
from datetime import datetime
import time
import ccxt

binance = ccxt.binance()

class Volatility_BS(object):
    def __init__(
        self,
        ask,
        open_now,
        high_past,
        low_past,
        
        k = 0.56,
    ):
        super().__init__()
        self.ask = float(ask)
        self.open_now = float(open_now)
        self.high_past = float(high_past)
        self.low_past = float(low_past)
        
        self.right_side = round(self.open_now + (self.high_past - self.low_past)*k, 2)
        # print(f"{self.open_now} + ( {self.high_past} - {self.low_past} ) * 0.5")
        # print(f"= {self.right_side}")
        print(f"{self.ask} > {self.right_side} ?")
    def VBS_calc(self):
        if self.ask > self.right_side:
            return True
        else: return False
        
class ccxt_dataIO:
    def __init__(
        self,
    ):
        pass
    def get_account():
        global binance
        file_path = os.path.dirname(os.path.abspath(__file__))
        account_path = os.path.normpath(os.path.join(file_path,"account.txt"))
        with open(account_path) as f:
            lines = f.readlines()
            api_key = lines[0].strip() 
            secret = lines[1].strip() 
        binance = ccxt.binance(config={
            'apiKey': api_key,
            'secret': secret
        })
    def parse_timeframe(timeframe):
        amount = int(timeframe[0:-1])
        unit = timeframe[-1]
        if 'y' == unit:
            scale = 60 * 60 * 24 * 365
        elif 'M' == unit:
            scale = 60 * 60 * 24 * 30
        elif 'w' == unit:
            scale = 60 * 60 * 24 * 7
        elif 'd' == unit:
            scale = 60 * 60 * 24
        elif 'h' == unit:
            scale = 60 * 60
        elif 'm' == unit:
            scale = 60
        elif 's' == unit:
            scale = 1
        else:
            raise print('timeframe unit {} is not supported'.format(unit))
        return amount * scale

        
def dailydo():
    global binance
    ccxt_dataIO.get_account()
    target_market = "ETH/BUSD"
    timeframe = "1h"
    
    timeframe_interval = ccxt_dataIO.parse_timeframe(timeframe)
    coin, fundamental = target_market.split("/")
    starttimestamp = datetime.now().timestamp() * 1000
    endtimestmap = starttimestamp + 7190000
    last_time = starttimestamp
    buy_or_not = False
    sell_or_not = False
    while True:
        if datetime.now().timestamp() >= endtimestmap:
            break
        sidecheck = binance.fetch_orders(symbol = target_market, since=None, limit = 1)[0]["side"]
        print(sidecheck)
        last_ohlcv = binance.fetch_ohlcv(target_market, timeframe=timeframe, since=None, limit=2)
        open_now = last_ohlcv[-1][1]
        high_past = last_ohlcv[-2][2]
        low_past = last_ohlcv[-2][3]
        print("open_now:", last_ohlcv[-1][1], end=",  ")
        print("high_past:", last_ohlcv[-2][2], end=",  ")
        print("low_past:", last_ohlcv[-2][3])
        
        
        while True:
            time.sleep(1.5)
            now_ticker = binance.fetch_ticker(target_market)
            ask = now_ticker["ask"]
            timestamp = now_ticker["timestamp"]
            
            # print("check loop part:")
            VBS_strategy = Volatility_BS(
                ask=ask,
                open_now=open_now,
                high_past=high_past,
                low_past=low_past,
            )
            # print(last_ohlcv[-1][0] + timeframe_interval*1000)
            # print(timestamp)
            # print("")
            if last_ohlcv[-1][0] + timeframe_interval*1000 <= timestamp:
                sell_or_not = True
                break
            
            buy_or_not = VBS_strategy.VBS_calc()
            if buy_or_not:
                break

                
        # print("local time: ",starttimestamp/1000, end=",  ")
        last_time = last_ohlcv[-1][0]
        
        if sell_or_not:
            if sidecheck == "sell":
                continue
            balance = binance.fetch_balance()
            coin_wallet = balance[coin]
            funda_wallet = balance[fundamental]
            print("sell func part:")
            print("coin-wallet: ", coin_wallet)
            print("base-wallet: ", funda_wallet)
            print(f"TOTAL BALANCE: {coin_wallet['total']*ask+funda_wallet['total']}")
            if coin_wallet["free"] == 0:
                print("None coin exist!")
                continue
            else:
                binance.create_market_sell_order(target_market, coin_wallet["free"])
                sidecheck = "sell"
                sell_or_not = False
                print("sell OCCUR!!!", end="\n \n")
                time.sleep(3)
                continue
        
        # print(ToF)
        if buy_or_not:
            if sidecheck == "buy":
                continue
            balance = binance.fetch_balance()
            coin_wallet = balance[coin]
            funda_wallet = balance[fundamental]
            print("buy func part:")
            print("coin-wallet: ", coin_wallet)
            print("base-wallet: ", funda_wallet)
            print(f"TOTAL BALANCE: {coin_wallet['total']*ask+funda_wallet['total']}")
            if funda_wallet["free"] == 0:
                print("None Cash exist!")
                continue
            else:
                amount = funda_wallet["free"] / ask
                time.sleep(0.3)
                binance.create_market_buy_order(target_market, amount)
                sidecheck = "buy"
                buy_or_not = False
                print("buy OCCUR!!!", end="\n \n")
                time.sleep(3)
                continue
            
        # print("last_ohlcv time: ",last_ohlcv[-2][0]/1000, end=", ")
        # print("last_time: ", last_time/1000, end=", ")
        # print("now_time: ", datetime.now().timestamp())
    
                

if __name__ == "__main__":
    schedule.every(1).seconds.do(dailydo)
    schedule.every(2).hours.do(dailydo)
    while True:
        schedule.run_pending()
        
    