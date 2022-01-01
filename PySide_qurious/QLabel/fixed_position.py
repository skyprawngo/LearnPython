# take overlap two widget, one is abs position, other is spacing frame

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 550)
        self.vlayout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.label.setFixedSize(400, 400)
        self.label.setStyleSheet("background-color: lightblue;")
        self.label.setAttribute(Qt.WA_TranslucentBackground) #have on and off you want

        
        self.vlayout.addWidget(self.label)
        
        self.label2 = QLabel(self)
        self.label2.setStyleSheet("background-color: darkgray;")
        self.label2.move(QPoint(50, 50))
        
        self.setLayout(self.vlayout)
        
        

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    