import os
import datetime 
import pandas as pd
import ccxt
import matplotlib.pyplot as plt 
import mplfinance as mpf 

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

def set_ohlcv_file(df = pd.DataFrame(), filename = "ohlcv.csv"):
    file_path = os.path.dirname(os.path.abspath(__file__))
    transaction_path = os.path.normpath(os.path.join(file_path, filename))
    if not os.path.isfile(transaction_path):
        df.to_csv(transaction_path)
    if not df.empty:
        df.to_csv(transaction_path)

def get_ohlcv_file(filename = "ohlcv.csv"):
    file_path = os.path.dirname(os.path.abspath(__file__))
    transaction_path = os.path.normpath(os.path.join(file_path, filename))
    df = pd.read_csv(transaction_path)
    return df

binance = get_account()

if True:
    ohlcv = binance.fetch_ohlcv("ETC/BUSD", timeframe="4h")
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df.set_index('timestamp', inplace=True)
    set_ohlcv_file(df)

df = get_ohlcv_file()
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
# print(df)
# df=df[200:]



# MA백태스팅 *.shift()를 사용해서도 한번 만들어볼것
for mnav in [10, 20, 30, 40, 50]:
    for i in range(len(df.index)):
        if i < mnav:
            continue
        df.at[i,mnav] = sum(df.iloc[i-mnav:i, 3])/mnav

df['close-50'] = df['close']-df[50]
df['10-20'] = df[10]-df[20]
df["Buy"] = (df['close-50']>0)&(df['close-50'].shift()<0)
df["Sell"] = (df['10-20']<0)&(df['10-20'].shift()>0)

# set_ohlcv_file(df, "bos_BNB.csv")

profit = 0
tradetime = 0
buyed = None
selled = None
for i in range(len(df.index)):
    if df.at[i, 'Buy']:
        buyed = df.at[i, 'close']
    if df.at[i, 'Sell'] and buyed:
        selled = df.at[i, 'close']
    if buyed and selled:
        profit += selled-buyed
        tradetime += 1
        buyed = None
        selled = None
        
print(profit)
print(tradetime)

# 차트 설정하기 
df.set_index('timestamp', inplace=True)
mpf.plot(df, 
        type='candle', # 캔들 차트 
        mav=(10, 20, 30, 40, 50), # 10일, 20일, 60일 이동평균선 표시 
        volume=True, #거래량 표시 
        style='yahoo', 
        figratio=(10,5),
        tight_layout=True) #좌우 공백 제거 
plt.show()