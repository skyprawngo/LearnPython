import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *

from py_grips import PyGrips
from sub1_grip import Grip

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.resize(1000,600)

        self.widget_1 = QWidget()
        self.widget_1_layout = QVBoxLayout(self.widget_1)
        self.widget_2 = Grip(self.widget_1, self)

        self.widget_1_layout.addWidget(self.widget_2)
        self.setCentralWidget(self.widget_1)
        self.setWindowTitle('Grip n Round Qurious')
        self.show()
    
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()