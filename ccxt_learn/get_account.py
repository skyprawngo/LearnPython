import os
import getpass
import pickle
import ccxt
import pandas as pd

def enroll_account_txt():
    username = getpass.getuser()
    account_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist/user_data.txt"))
    with open(account_path, "rb") as reader:
        data = pickle.load(reader)
        key = [data["apikey"], data["secretkey"]]
    binance = ccxt.binance(config={
        'apiKey': key[0],
        'secret': key[1]
    })
    return binance

appdata_record_path = os.path.normpath("C:/Users/skypr/AppData/Local/Stretegist/record.csv")
def load_AppData_record():
    try:
        record = pd.read_csv(appdata_record_path)
    except:
        record = pd.DataFrame()
    return record

if __name__ == "__main__":
    enroll_account_txt()