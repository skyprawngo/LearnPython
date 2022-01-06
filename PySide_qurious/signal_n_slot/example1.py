import sys, time
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MySignal(QObject):
    signal = Signal(str)

    def __init__(self, num):
        super().__init__()
        self.num = num
    
    def sendNum(self):
        self.signal.emit(str(self.num))

class NumberedButton(QPushButton):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.setText(str(num))
        self.btn_signal = MySignal(num)
        
        self.clicked.connect(self.btn_signal.sendNum)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.vlayout = QVBoxLayout()
        self.llineedit = QLineEdit()
        self.vlayout.addWidget(self.llineedit)
        
        for i in range(5):
            btn = NumberedButton(i)
            self.vlayout.addWidget(btn)

            btn.btn_signal.signal.connect(self.llineedit.setText)

        self.centralwidget.setLayout(self.vlayout)
        self.setCentralWidget(self.centralwidget)

if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()