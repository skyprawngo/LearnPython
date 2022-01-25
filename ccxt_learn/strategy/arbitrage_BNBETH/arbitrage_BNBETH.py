import os
from re import A
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
        
def dailydo():
    market = {"num": "BNB", "den": "ETH"}
    set_dir_file()
    binance = get_account()
    current_balance = binance.fetch_balance()
    print(current_balance[market["num"]])
    print(current_balance[market["den"]])
    
    

if __name__ == "__main__":
    # schedule.every(2).seconds.do(dailydo)
    # schedule.every().day.at("10:00").do(dailydo)
    # while True: 
    #     schedule.run_pending() 
    #     time.sleep(1)

    dailydo()