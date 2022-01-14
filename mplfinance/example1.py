import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
import mplfinance as mpf

yf.pdr_override()
start_dt = dt.datetime(2021, 12, 1)
end_dt = dt.datetime.now()

df = pdr.get_data_yahoo("AAPL", start_dt, end_dt)
df = df.loc[:, ["Open", "High", "Low", "Adj Close", "Volume"]]
df = df.rename(columns={"Adj Close": "Close"})

mc = mpf.make_marketcolors(up="r", down="b")
s = mpf.make_mpf_style(base_mpf_style='starsandstripes', marketcolors=mc)
# mpf.plot(df, type="candle", style=s, title="AAPL")

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        global s
        super(MainWindow, self).__init__()
        self.label = Qwidget(s)
        
        self.setCentralWidget(self.label)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    