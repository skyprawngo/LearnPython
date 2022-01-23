import os
from re import A
import time
from datetime import datetime
import schedule
import pandas as pd
import numpy as np
import ccxt

def get_account():
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
    return binance
        
def dailydo():
    ideal_rate = {
        "BTC": 0.2,
        "ETH": 0.2,
        "BNB": 0.5,
        "SOL": 0.1,
    }
    df_rate = pd.Series(ideal_rate, name="ideal_rate")
    
    binance = get_account()
    current_balance = binance.fetch_balance()
    coin_list = []
    for wallet_coin in current_balance["total"]:
        if not current_balance["total"][wallet_coin] == 0:
            coin_list.append(wallet_coin)
            
    coin_list = list(set(ideal_rate.keys())|set(coin_list))
    df_BUSD = pd.DataFrame(index=coin_list)
    ask = []
    total_price = 0
    for coin in coin_list:
        if not coin == "BUSD":
            ticker = binance.fetch_ticker(f"{coin}/BUSD")
        else:
            ticker = {}
            ticker["ask"] = 1
        amount = current_balance[coin]["total"]
        ask.append(ticker["ask"])
        df_BUSD.loc[coin,"ask"] = ticker["ask"]
        df_BUSD.loc[coin,"amount"] = amount
        df_BUSD.loc[coin,"value(USD)"] = ticker["ask"]*amount
        total_price += ticker["ask"]*amount
    df = pd.concat([df_BUSD,df_rate], axis = 1)
    df = df.fillna(0)
    current_rate = {}
    for coin in coin_list:
        current_rate[coin] = df_BUSD.loc[coin,"value(USD)"]/total_price
    df.insert(3, "current_rate", current_rate.values())

    df_transfer = pd.DataFrame()
    df_transfer["tr_rate"] = df["current_rate"] - df["ideal_rate"]
    print(df)
    print(total_price)
    
    for coin in df_transfer.index:
        df_transfer.at[coin, "tr_price(USD)"] = int(df_transfer.loc[coin, "tr_rate"] * total_price)
        if not df_transfer.loc[coin, "tr_price(USD)"] == 0:
            df_transfer.at[coin, "tr_amount"] = df_transfer.loc[coin, "tr_price(USD)"] / df.loc[coin, "ask"]
            
    df_transfer = df_transfer.fillna(0)
    
    funda = ["BNB", "BUSD"]
    tr_number = 0
    
    for coin in df_transfer.index:
        if df_transfer.loc[coin, "tr_price(USD)"] > 0 and not coin == "BNB" :
            # 여기에 BNB로 코인 이동시키는 함수 작성
            print(coin)
    
    for coin in df_transfer.index:
        if df_transfer.loc[coin, "tr_price(USD)"] < 0 and not coin == "BNB" :
            # 여기에 비율 모자란 코인들을 BNB월렛애서 매꿔주는 함수 작성
            print(coin)
    print(df_transfer)
    pass

if __name__ == "__main__":
    # schedule.every(2).seconds.do(dailydo)
    # schedule.every().day.at("10:00").do(dailydo)
    # while True: 
    #     schedule.run_pending() 
    #     time.sleep(1)

    dailydo()