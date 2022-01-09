from re import M
import ccxt
import pprint
from ccxt_communicator import CCXT_Binance
from get_account import *

binance = enroll_account_txt()
that_time = binance.parse8601("2021-06-12T00:00:00Z")
# print(binance.parse8601("2020-06-12T00:00:00Z"))
# time = binance.iso8601(that_time)
# print(time)

mytrades = binance.fetch_my_trades(symbol="BNB/ETH", since=that_time, limit=1)

for mytrade in mytrades:
    pprint.pprint(mytrade)