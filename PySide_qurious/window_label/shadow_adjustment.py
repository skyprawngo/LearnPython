from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pywindow import PyWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        
        self.setContentsMargins(10,10,10,10)
        pywindow = PyWindow(
            self,
            startup_size=[1000, 600],
            minimum_size=[500, 300]
        )
        self.setCentralWidget(pywindow)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    