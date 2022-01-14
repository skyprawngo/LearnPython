import sys
from PySide6.QtCharts import QCandlestickSeries, QChart, QChartView, QCandlestickSet
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QPointF
from PySide6 import QtCharts as qc
import pandas as pd

data = ((1, 7380, 7520, 7380, 7510, 7324), 
    (2, 7520, 7580, 7410, 7440, 7372),
    (3, 7440, 7650, 7310, 7520, 7434),
    (4, 7450, 7640, 7450, 7550, 7480),
    (5, 7510, 7590, 7460, 7490, 7502),
    (6, 7500, 7590, 7480, 7560, 7512),
    (7, 7560, 7830, 7540, 7800, 7584))

df = pd.DataFrame(data)
print(df)
app = QApplication(sys.argv)
#
series = QCandlestickSeries()
series.setDecreasingColor(Qt.blue)
series.setIncreasingColor(Qt.red)

ma5 = qc.QLineSeries()  # 5-days average data line
tm = []  # stores str type data

# in a loop,  series and ma5 append corresponding data
for num, o, h, l, c, m in data:
    series.append(QCandlestickSet(o, h, l, c))
    ma5.append(QPointF(num, m))
    tm.append(str(num))

stick = QCandlestickSet(df[0][0], df[0][1], df[0][2], df[0][3])
print(stick)

chart = QChart()

chart.addSeries(series)  # candle
chart.addSeries(ma5)  # ma5 line

chart.setAnimationOptions(QChart.SeriesAnimations)
chart.createDefaultAxes()
chart.legend().hide()

chart.axisX(series).setCategories(tm)
chart.axisX(ma5).setVisible(False)

chartview = QChartView(chart)
ui = QMainWindow()
ui.setGeometry(50, 50, 500, 300)
ui.setCentralWidget(chartview)
ui.show()
app.exec()