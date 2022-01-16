# VBS - Volatility Breakthrough Strategy. 변동성 돌파 전략 구현하기
import os
import schedule
from datetime import datetime
import time
import ccxt

binance = ccxt.binance()
weight = 0

class VBS_Strategy:
    def VBS_calc(
        ask,
        open_now,
        high_last,
        low_last,
        k = 0.51,
    ):
        right_side = round(open_now + (high_last - low_last)*k, 2)
        print(f"{ask} > {right_side} ? ")
        if ask > right_side:
            return True
        else: return False
        
class Data_Process:
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
    
    def buyprocess(
        ticker,
    ):
        global binance, weight
        ask = ticker["ask"]
        market = ticker["symbol"]
        coin, funda = market.split("/")
        
        balance = binance.fetch_balance()
        wallet_coin = balance[coin]
        wallet_funda = balance[funda]
        
        if wallet_funda["free"] == 0:
            print("None Cash exist!")
            return False
        else:
            amount = wallet_funda["free"] / ask
            order = binance.create_market_buy_order(market, amount)
            time.sleep(3)
            print("TIME: ", end="")
            print(ticker["datetime"])
            print("buy OCCUR!!!", end="\n \n")
            return True
    
    def sellprocess(
        ticker,
    ):
        global binance, weight
        market = ticker["symbol"]
        coin, funda = market.split("/")
        
        balance = binance.fetch_balance()
        wallet_coin = balance[coin]
        wallet_funda = balance[funda]
        
        if wallet_coin["free"] == 0:
            print("None Coin exist!")
            return False
        else:
            amount = wallet_coin["free"]
            order = binance.create_market_sell_order(market, amount)
            print("sell OCCUR!!!", end="\n \n")
            time.sleep(3)
            return True
    
def dailydo():
    global binance
    market = "ETH/BUSD"
    timeframe = "1h"
    timeintervalms = Data_Process.parse_timeframe(timeframe)*1000
    is_buy = False
    is_sell = False
    
    Data_Process.get_account()
    order_last = binance.fetch_my_trades(market, since=None, limit=1)
    if order_last[-1]["side"] == "buy":
        buyed = True
        selled = False
    elif order_last[-1]["side"] == "sell":
        buyed = False
        selled = True
    
    # timeframe당 한번 루프
    while True:
        ohlcv = binance.fetch_ohlcv(market, timeframe=timeframe, since=None, limit=2)
        open_timestamp = ohlcv[-1][0]
        open_now = ohlcv[-1][1]
        high_last = ohlcv[-2][2]
        low_last = ohlcv[-2][3]
        ask_list = []
        
        # buy판단
        while True:
            ticker = binance.fetch_ticker(market)
            ask_list.append(ticker["ask"])
            if ticker["timestamp"] > open_timestamp+timeintervalms:
                ohlcv = binance.fetch_ohlcv(market, timeframe=timeframe, since=None, limit=2)
                open_timestamp = ohlcv[-1][0]
                open_now = ohlcv[-1][1]
                high_last = ohlcv[-2][2]
                low_last = ohlcv[-2][3]
    
            is_buy = VBS_Strategy.VBS_calc(
                ask = ticker["ask"],
                open_now = open_now,
                high_last = high_last,
                low_last = low_last,
            )
            if is_buy:
                buyed = Data_Process.buyprocess(
                    ticker = ticker,
                )
                ask_buyed = ticker["ask"]
                break
            
            time.sleep(5)
        
        # sell 판단
        while True:
            is_sell = False
            ticker = binance.fetch_ticker(market)
            
            ask_list.append(ticker["ask"])
                
            if ticker["timestamp"] > open_timestamp+timeintervalms:
                is_sell = True
            if ask_list[-3]>ask_list[-2]>ask_list[-1] and ask_list[-1]>ask_buyed:
                is_sell = True
                
            if is_sell:
                selled = Data_Process.sellprocess(
                    ticker = ticker,
                )
                is_sell = False
                break
            
            time.sleep(1)
        
        # sell 하면 남은 timeframe은 판단 안함
        while True:
            ticker = binance.fetch_ticker(market)
            if ticker["timestamp"] > open_timestamp+timeintervalms:
                break
            time.sleep(10)
            
                

if __name__ == "__main__":
    schedule.every(1).seconds.do(dailydo)
    schedule.every(2).hours.do(dailydo)
    while True:
        schedule.run_pending()
    
    
    
    # ticker = binance.fetch_ticker("ETH/BUSD")
    # print(ticker)

    # ohlcv = binance.fetch_ohlcv("ETH/BUSD", timeframe="1h", since=None, limit=2)
    # # print(ohlcv)
    
    # Data_Process.get_account()
    # last_order = binance.fetch_my_trades("ETH/BUSD", since=None, limit=1)
    # print(last_order)
    
    # balance = binance.fetch_balance()
    # print(balance)
    