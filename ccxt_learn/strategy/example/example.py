from pykrx import stock 
import pandas as pd 
import mplfinance as mpf 
import numpy as np 
import plotly.graph_objects as go 
import plotly.subplots as ms 
import plotly.express as px

# 전체 종목코드와 종목명 가져오기 
stock_list = pd.DataFrame({'종목코드':stock.get_market_ticker_list(market="ALL")}) 
stock_list['종목명'] = stock_list['종목코드'].map(lambda x: stock.get_market_ticker_name(x)) 

# stock_name의 2021년 주가 데이터 가져오기 
stock_name = "삼성전자" 
stock_from = "20201220" 
stock_to = "20220128" 
ticker = stock_list.loc[stock_list['종목명']== stock_name, '종목코드'] 
df = stock.get_market_ohlcv_by_date(fromdate=stock_from, todate=stock_to, ticker=ticker) 

# 칼럼명을 영문명으로 변경
df = df.rename(columns={'시가':'Open', '고가':'High', '저가':'Low', '종가':'Close', '거래량':'Volume'}) 
df["Close"]=df["Close"].apply(pd.to_numeric,errors="coerce")

# 볼린저밴드 구하기 
df['ma20'] = df['Close'].rolling(window=20).mean() # 20일 이동평균 
df['stddev'] = df['Close'].rolling(window=20).std() # 20일 이동표준편차 
df['upper'] = df['ma20'] + 2*df['stddev'] # 상단밴드 
df['lower'] = df['ma20'] - 2*df['stddev'] # 하단밴드

# MACD 구하기 
df['ma12'] = df['Close'].rolling(window=12).mean() # 12일 이동평균 
df['ma26'] = df['Close'].rolling(window=26).mean() # 26일 이동평균 
df['MACD'] = df['ma12'] - df['ma26'] # MACD 
df['MACD_Signal'] = df['MACD'].rolling(window=9).mean() # MACD Signal(MACD 9일 이동평균) 
df['MACD_Oscil'] = df['MACD'] - df['MACD_Signal'] #MACD 오실레이터

# 스토캐스틱 구하기 
df['ndays_high'] = df['High'].rolling(window=14, min_periods=1).max() # 14일 중 최고가 
df['ndays_low'] = df['Low'].rolling(window=14, min_periods=1).min() # 14일 중 최저가 
df['fast_k'] = (df['Close'] - df['ndays_low']) / (df['ndays_high'] - df['ndays_low']) * 100 # Fast %K 구하기 
df['slow_d'] = df['fast_k'].rolling(window=3).mean() # Slow %D 구하기

# MFI 구하기 
df['PB'] = (df['Close'] - df['lower']) / (df['upper'] - df['lower']) 
df['TP'] = (df['High'] + df['Low'] + df['Close']) / 3 
df['PMF'] = 0 
df['NMF'] = 0 
for i in range(len(df.Close)-1): 
    if df.TP.values[i] < df.TP.values[i+1]: 
        df.PMF.values[i+1] = df.TP.values[i+1] * df.Volume.values[i+1] 
        df.NMF.values[i+1] = 0 
    else: 
        df.NMF.values[i+1] = df.TP.values[i+1] * df.Volume.values[i+1] 
        df.PMF.values[i+1] = 0 
        df['MFR'] = (df.PMF.rolling(window=10).sum() / df.NMF.rolling(window=10).sum()) 
        df['MFI10'] = 100 - 100 / (1 + df['MFR'])

df['II'] = (2*df['Close']-df['High']-df['Low'])/(df['High']-df['Low'])*df['Volume'] 
df['IIP21'] = df['II'].rolling(window=21).sum()/df['Volume'].rolling(window=21).sum()*100

U = np.where(df['Close'].diff(1) > 0, df['Close'].diff(1), 0) 
D = np.where(df['Close'].diff(1) < 0, df['Close'].diff(1) *(-1), 0) 
AU = pd.DataFrame(U, index=df.index).rolling(window=14).mean() 
AD = pd.DataFrame(D, index=df.index).rolling(window=14).mean() 
RSI = AU / (AD+AU) *100 
df['RSI'] = RSI

df = df[25:]


candle = go.Candlestick(x=df.index,open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'], increasing_line_color = 'red',decreasing_line_color = 'blue', showlegend=False)
upper = go.Scatter(x=df.index, y=df['upper'], line=dict(color='red', width=2), name='upper', showlegend=False)
ma20 = go.Scatter(x=df.index, y=df['ma20'], line=dict(color='black', width=2), name='ma20', showlegend=False)
lower = go.Scatter(x=df.index, y=df['lower'], line=dict(color='blue', width=2), name='lower', showlegend=False)

Volume = go.Bar(x=df.index, y=df['Volume'], marker_color='red', name='Volume', showlegend=False)

MACD = go.Scatter(x=df.index, y=df['MACD'], line=dict(color='blue', width=2), name='MACD', legendgroup='group2', legendgrouptitle_text='MACD')
MACD_Signal = go.Scatter(x=df.index, y=df['MACD_Signal'], line=dict(dash='dashdot', color='green', width=2), name='MACD_Signal')
MACD_Oscil = go.Bar(x=df.index, y=df['MACD_Oscil'], marker_color='purple', name='MACD_Oscil')

fast_k = go.Scatter(x=df.index, y=df['fast_k'], line=dict(color='skyblue', width=2), name='fast_k', legendgroup='group3', legendgrouptitle_text='%K %D')
slow_d = go.Scatter(x=df.index, y=df['slow_d'], line=dict(dash='dashdot', color='black', width=2), name='slow_d')

PB = go.Scatter(x=df.index, y=df['PB']*100, line=dict(color='blue', width=2), name='PB', legendgroup='group4', legendgrouptitle_text='PB, MFI')
MFI10 = go.Scatter(x=df.index, y=df['MFI10'], line=dict(dash='dashdot', color='green', width=2), name='MFI10')

RSI = go.Scatter(x=df.index, y=df['RSI'], line=dict(color='red', width=2), name='RSI', legendgroup='group5', legendgrouptitle_text='RSI')
 
# 스타일 
fig = ms.make_subplots(rows=5, cols=2, specs=[[{'rowspan':4},{}],[None,{}],[None,{}],[None,{}],[{},{}]], shared_xaxes=True, horizontal_spacing=0.03, vertical_spacing=0.01) 
fig.add_trace(candle,row=1,col=1) 
fig.add_trace(upper,row=1,col=1) 
fig.add_trace(ma20,row=1,col=1) 
fig.add_trace(lower,row=1,col=1) 
fig.add_trace(Volume,row=5,col=1) 
fig.add_trace(candle,row=1,col=2) 
fig.add_trace(upper,row=1,col=2) 
fig.add_trace(ma20,row=1,col=2) 
fig.add_trace(lower,row=1,col=2) 
fig.add_trace(MACD,row=2,col=2) 
fig.add_trace(MACD_Signal,row=2,col=2) 
fig.add_trace(MACD_Oscil,row=2,col=2) 
fig.add_trace(fast_k,row=3,col=2) 
fig.add_trace(slow_d,row=3,col=2) 
fig.add_trace(PB,row=4,col=2) 
fig.add_trace(MFI10,row=4,col=2) 
fig.add_trace(RSI,row=5,col=2) 

# 추세추종 
for i in range(len(df['Close'])): 
    if df['PB'][i] > 0.8 and df['MFI10'][i] > 80: 
        trend_fol = go.Scatter(x=[df.index[i]], y=[df['Close'][i]], marker_color='orange', marker_size=20, marker_symbol='triangle-up', opacity=0.7, showlegend=False) 
        fig.add_trace(trend_fol,row=1,col=1) 
    elif df['PB'][i] < 0.2 and df['MFI10'][i] < 20: 
        trend_fol = go.Scatter(x=[df.index[i]], y=[df['Close'][i]], marker_color='darkblue', marker_size=20, marker_symbol='triangle-down', opacity=0.7, showlegend=False) 
        fig.add_trace(trend_fol,row=1,col=1) 

# 역추세추종 
for i in range(len(df['Close'])): 
    if df['PB'][i] < 0.05 and df['IIP21'][i] > 0: 
        trend_refol = go.Scatter(x=[df.index[i]], y=[df['Close'][i]], marker_color='purple', marker_size=20, marker_symbol='triangle-up', opacity=0.7, showlegend=False) #보라 
        fig.add_trace(trend_refol,row=1,col=1) 
    elif df['PB'][i] > 0.95 and df['IIP21'][i] < 0: 
        trend_refol = go.Scatter(x=[df.index[i]], y=[df['Close'][i]], marker_color='skyblue', marker_size=20, marker_symbol='triangle-down', opacity=0.7, showlegend=False) #하늘 
        fig.add_trace(trend_refol,row=1,col=1)
        
fig.update_layout(autosize=True, xaxis1_rangeslider_visible=False, xaxis2_rangeslider_visible=False, margin=dict(l=50,r=50,t=50,b=50), template='seaborn', title=f'{stock_name}({int(ticker.values)})의 날짜: {stock_to} [추세추종전략:오↑파↓] [역추세전략:보↑하↓]') 
fig.update_xaxes(tickformat='%y년%m월%d일', zeroline=True, zerolinewidth=1, zerolinecolor='black', showgrid=True, gridwidth=2, gridcolor='lightgray', showline=True,linewidth=2, linecolor='black', mirror=True) 
fig.update_yaxes(tickformat=',d', zeroline=True, zerolinewidth=1, zerolinecolor='black', showgrid=True, gridwidth=2, gridcolor='lightgray',showline=True,linewidth=2, linecolor='black', mirror=True) 
fig.update_traces(xhoverformat='%y년%m월%d일') 

config = dict({'scrollZoom': True}) 
fig.show(config=config)