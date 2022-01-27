import os
import time
from datetime import datetime
import schedule
import pandas as pd
import numpy as np
import ccxt

def get_account():
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    account_path = os.path.normpath(os.path.join(file_path,"account.txt"))
    with open(account_path) as f:
        lines = f.readlines()
        api_key = lines[0].strip() 
        secret = lines[1].strip() 
    binance = ccxt.binance(config={
        'apiKey': api_key,
        'secret': secret
    })
    return binance

def set_dir_file(df = pd.DataFrame()):
    file_path = os.path.dirname(os.path.abspath(__file__))
    transaction_path = os.path.normpath(os.path.join(file_path,"transaction.csv"))
    if not os.path.isfile(transaction_path):
        df.to_csv(transaction_path)
    if not df.empty:
        df.to_csv(transaction_path)

def get_dir_file():
    file_path = os.path.dirname(os.path.abspath(__file__))
    transaction_path = os.path.normpath(os.path.join(file_path,"transaction.csv"))
    df = pd.read_csv(transaction_path)
    return df

def dailydo():
    market = {"num": "BNB", "den": "ETH"}
    set_dir_file()
    binance = get_account()
    current_balance = binance.fetch_balance()
    print("BNB: ", current_balance[market["num"]])
    print("ETH: ", current_balance[market["den"]])
    
    wlt_num = current_balance[market["num"]]
    wlt_den = current_balance[market["den"]]
    symbol = f"{market['num']}/{market['den']}"
    ticker = binance.fetch_ticker(symbol)
    ticker.pop("info")
    print(ticker)
    BNB_tot = wlt_num["total"] + ticker["ask"] * wlt_den["total"]
    print(BNB_tot)
    onetry_amount = BNB_tot / 10
    print(round(onetry_amount, 3))
    
    df = get_dir_file()
    if df.empty and ticker["ask"]*wlt_den["total"] > onetry_amount:
        # order = binance.create_market_buy_order(symbol, amount=onetry_amount)
        pass
    elif ticker["ask"]*wlt_den["total"] < onetry_amount:
        # order = binance.create_market_sell_order(symbol, amount=onetry_amount)
        pass
    
    order = binance.fetch_order(id = 573295877, symbol=symbol)
    order.pop("info")
    print(order)
    
    # df_order = pd.DataFrame(order)
    # df = df.append(df_order)
    # print(df)
    # set_dir_file(df)
    

if __name__ == "__main__":
    # schedule.every(2).seconds.do(dailydo)
    # schedule.every().day.at("10:00").do(dailydo)
    # while True: 
    #     schedule.run_pending() 
    #     time.sleep(1)

    dailydo()