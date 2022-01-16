import os
import schedule
import pandas as pd
import numpy as np
import ccxt

binance = ccxt.binance()
class Data_IO:
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
            
    def df_save(df, symbol):
        name = symbol.replace("/", "_")
        file_path = os.path.dirname(os.path.abspath(__file__))
        df_path = os.path.normpath(os.path.join(file_path,f"{name}.csv"))
        df.to_csv(df_path, index=False)
        pass
    
    def df_load(symbol):
        name = symbol.replace("/", "_")
        file_path = os.path.dirname(os.path.abspath(__file__))
        df_path = os.path.normpath(os.path.join(file_path,f"{name}.csv"))
        df = pd.read_csv(df_path)
        return df

def get_historical_data(symbol, start_date):

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
    
    ohlcv = binance.fetch_ohlcv("BTC/BUSD", timeframe="1h")
    df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    return df

tsla = get_historical_data('TSLA', '2020-01-01')

# SUPERTREND CALCULATION
def get_supertrend(high, low, close, lookback, multiplier):
    
    # ATR
    
    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift(1)))
    tr3 = pd.DataFrame(abs(low - close.shift(1)))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis = 1, join = 'inner').max(axis = 1)
    atr = tr.ewm(lookback).mean()
    
    # H/L AVG AND BASIC UPPER & LOWER BAND
    
    hl_avg = (high + low) / 2
    upper_band = (hl_avg + multiplier * atr).dropna()
    lower_band = (hl_avg - multiplier * atr).dropna()
    
    # FINAL UPPER BAND
    
    final_bands = pd.DataFrame(columns = ['upper', 'lower'])
    final_bands.iloc[:,0] = [x for x in upper_band - upper_band]
    final_bands.iloc[:,1] = final_bands.iloc[:,0]

    for i in range(len(final_bands)):
        if i == 0:
            final_bands.iloc[i,0] = 0
        else:
            if (upper_band[i] < final_bands.iloc[i-1,0]) | (close[i-1] > final_bands.iloc[i-1,0]):
                final_bands.iloc[i,0] = upper_band[i]
            else:
                final_bands.iloc[i,0] = final_bands.iloc[i-1,0]
    
    # FINAL LOWER BAND
    
    for i in range(len(final_bands)):
        if i == 0:
            final_bands.iloc[i, 1] = 0
        else:
            if (lower_band[i] > final_bands.iloc[i-1,1]) | (close[i-1] < final_bands.iloc[i-1,1]):
                final_bands.iloc[i,1] = lower_band[i]
            else:
                final_bands.iloc[i,1] = final_bands.iloc[i-1,1]
    
    # SUPERTREND
    
    supertrend = pd.DataFrame(columns = [f'supertrend_{lookback}'])
    supertrend.iloc[:,0] = [x for x in final_bands['upper'] - final_bands['upper']]
    
    for i in range(len(supertrend)):
        if i == 0:
            supertrend.iloc[i, 0] = 0
        elif supertrend.iloc[i-1, 0] == final_bands.iloc[i-1, 0] and close[i] < final_bands.iloc[i, 0]:
            supertrend.iloc[i, 0] = final_bands.iloc[i, 0]
        elif supertrend.iloc[i-1, 0] == final_bands.iloc[i-1, 0] and close[i] > final_bands.iloc[i, 0]:
            supertrend.iloc[i, 0] = final_bands.iloc[i, 1]
        elif supertrend.iloc[i-1, 0] == final_bands.iloc[i-1, 1] and close[i] > final_bands.iloc[i, 1]:
            supertrend.iloc[i, 0] = final_bands.iloc[i, 1]
        elif supertrend.iloc[i-1, 0] == final_bands.iloc[i-1, 1] and close[i] < final_bands.iloc[i, 1]:
            supertrend.iloc[i, 0] = final_bands.iloc[i, 0]
    
    supertrend = supertrend.set_index(upper_band.index)
    supertrend = supertrend.dropna()[1:]
    
    # ST UPTREND/DOWNTREND
    
    upt = []
    dt = []
    close = close.iloc[len(close) - len(supertrend):]
    print(supertrend)
    for i in range(len(supertrend)):
        if close[i] > supertrend.iloc[i, 0]:
            upt.append(supertrend.iloc[i, 0])
            dt.append(np.nan)
        elif close[i] < supertrend.iloc[i, 0]:
            upt.append(np.nan)
            dt.append(supertrend.iloc[i, 0])
        else:
            upt.append(np.nan)
            dt.append(np.nan)
            
    st, upt, dt = pd.Series(supertrend.iloc[:, 0]), pd.Series(upt), pd.Series(dt)
    upt.index, dt.index = supertrend.index, supertrend.index
    
    return st, upt, dt

def dailydo():
    pass

if __name__ == "__main__":
    # schedule.every(1).seconds.do(dailydo)
    # schedule.every(2).hours.do(dailydo)
    # while True:
    #     schedule.run_pending()
    
    # binance = ccxt.binance()
    # ohlcv = binance.fetch_ohlcv("BTC/BUSD", timeframe="1d")
    # df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    # df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    # Data_IO.df_save(df, "BTC/BUSD")
    
    df = Data_IO.df_load("BTC/BUSD")

    st = pd.DataFrame()
    st['st'], st['s_upt'], st['st_dt'] = get_supertrend(df['high'], df['low'], df['close'], 10, 3)
    