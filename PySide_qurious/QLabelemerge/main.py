import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *

from btn_1 import Btn_1

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI(self)

    def init_UI(self, UiMainWindow):
        if not UiMainWindow.objectName():
            UiMainWindow.setObjectName(u"MainWindow")
        
        UiMainWindow.resize(
                1000, 600
        )
        
        UiMainWindow.setMinimumSize(
                500, 300
        )
        self.centralwidget = QWidget(UiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)

        self.centralwidget_vlayout = QVBoxLayout(self.centralwidget)
        self.frame_1 = QFrame()
        self.frame_1_vlayout = QVBoxLayout(self.frame_1)
        self.btn_1 = Btn_1(
            parent = self.frame_1,
            app_parent = UiMainWindow
        )
        
        self.frame_1_vlayout.addWidget(self.btn_1)
        self.centralwidget_vlayout.addWidget(self.frame_1)

        QMetaObject.connectSlotsByName(UiMainWindow)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle('MainWindow')
        self.show()

    

    

if __name__ == '__main__':
    app = QApplication()
    ex = MyApp()
    app.exec()