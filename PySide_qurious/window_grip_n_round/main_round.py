import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.widget_1 = QWidget()
        self.widget_1_layout = QVBoxLayout(self.widget_1)
        self.resize(1000,600)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.widget_1.setStyleSheet('''
            background-color: #849209;
            border-radius: 8px;
        ''')
        self.setCentralWidget(self.widget_1)
        self.setWindowTitle('Round Qurious')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()