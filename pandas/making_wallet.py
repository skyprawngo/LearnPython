import os
import sys
import ccxt
import pprint
import pandas as pd
sys.path.append(os.path.abspath(os.path.dirname(__name__)))
from ccxt_learn.get_account import *

binance = enroll_account_txt()

# df_history = load_AppData_record()

balance = binance.fetch_balance()
balance_total = balance["total"]
del_parameters = ["info", "free", "used", "total"]
for del_parameter in del_parameters:
    del balance[del_parameter]

for coin in balance_total.keys():
    if balance_total[coin] == 0:
        del balance[coin]
        
pprint.pprint(balance)

df_balance = pd.DataFrame(balance)
print(df_balance)


