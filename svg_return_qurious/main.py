import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.resize(1000,600)
        vlayout = QVBoxLayout()
              
        label_1 = QLabel()

        lebel_1_vlayout = QVBoxLayout(label_1)
        
        svg_1 = QSvgWidget()
        svg_1.setStyleSheet("background-color: lightblue")
        svg_1.setFixedWidth(80)
        svg_1.load("C:/pywork/anything/svg_return_qurious/logo_top_80_30.svg")
        
        print("here we are,",svg_1.height())
        
        lebel_1_vlayout.addWidget(svg_1)
        vlayout.addWidget(label_1)

        self.setLayout(vlayout)
        self.setWindowTitle('QSvgWidget')
        self.move(1500, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()