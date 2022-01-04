from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 600)
        self.qwidget = QWidget()
        self.verticalLayout = QVBoxLayout(self.qwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.scrollArea = QScrollArea(self.qwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 763, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1000))
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)
        
        self.setCentralWidget(self.qwidget)
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    