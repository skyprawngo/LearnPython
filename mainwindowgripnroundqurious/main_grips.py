import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *

from py_grips import PyGrips

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left_grip = PyGrips(self, "left")
        self.right_grip = PyGrips(self, "right")
        self.top_grip = PyGrips(self, "top")
        self.bottom_grip = PyGrips(self, "bottom")
        self.top_left_grip = PyGrips(self, "top_left")
        self.top_right_grip = PyGrips(self, "top_right")
        self.bottom_left_grip = PyGrips(self, "bottom_left")
        self.bottom_right_grip = PyGrips(self, "bottom_right")
        self.init_UI()

    def init_UI(self):
        self.widget_1 = QWidget()
        self.widget_1_layout = QVBoxLayout(self.widget_1)
        self.resize(1000,600)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.widget = QWidget()
        self.widget.setStyleSheet('''
            background-color: #849209;
            border-radius: 8px;
        ''')

        self.widget_1_layout.addWidget(self.widget)

        self.setCentralWidget(self.widget_1)
        self.setWindowTitle('Grip n Round Qurious')
        self.resize_grips()
        self.show()
    
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

    def resizeEvent(self, event):
        self.resize_grips(self)

    def resize_grips(self):
        self.left_grip.setGeometry(5, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
        self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
        self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
        self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
        self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
        self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()