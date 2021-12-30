import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        label_1_layout = QVBoxLayout()
        label_1_layout.setAlignment(Qt.AlignCenter)
        svg_1 = QSvgWidget()
        # svg_1.setStyleSheet("background-color: lightblue")
        svg_1.setFixedSize(80, 30)
        svg_1.load("C:/pywork/anything/PySide_qurious/svg_return/logo_top_80_30.svg")
        
        label_1_layout.addWidget(svg_1)
        
        print("here we are,",svg_1.height())
        
        self.setLayout(label_1_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('QSvgWidget')
        self.resize(1000,600)
        self.move(300, 300)
        
        
        widget1 = MyWidget()
        self.setCentralWidget(widget1)
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()