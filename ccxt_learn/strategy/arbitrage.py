import os
import schedule
from datetime import datetime
import time
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
    binance = get_account()
    current_balance = binance.fetch_balance()
    coin_list = []
    for wallet_coin in current_balance["total"]:
        if not current_balance["total"][wallet_coin] == 0:
            coin_list.append(wallet_coin)
    print(coin_list)
    
    pass

if __name__ == "__main__":
    schedule.every(2).seconds.do(dailydo)
    schedule.every().day.at("10:00").do(dailydo)
    while True: 
        schedule.run_pending() 
        time.sleep(1)
