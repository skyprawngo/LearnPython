from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800,600)
        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        self.scrollarea = QScrollArea()
        self.scrollarea.setStyleSheet('background-color: "#919191"')
        self.scrollarea_frame = QFrame()
        self.scrollarea_frame.setStyleSheet('background-color: darkgray')
        self.scrollarea_frame.setFixedHeight(1000)
        self.scrollarea_glayout = QGridLayout(self.scrollarea_frame)
        
        self.frame1 = QFrame()
        self.frame1.setStyleSheet("background-color: red;")
        self.scrollarea_glayout.addWidget(self.frame1, 0, 0)
        
        self.frame2 = QFrame()
        self.frame2.setStyleSheet("background-color: blue;")
        self.scrollarea_glayout.addWidget(self.frame2, 1, 0)
        
        self.scrollarea.setWidget(self.scrollarea_frame)
        self.vlayout.addWidget(self.scrollarea)
        self.setLayout(self.vlayout)
        
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    