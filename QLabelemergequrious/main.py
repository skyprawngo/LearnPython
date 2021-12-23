import sys

from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.theme = "dafault"
        
        self.centralwidget = QWidget()
        self.centralwidget_layout = QHBoxLayout(self.centralwidget)
        self.btn_1 = QPushButton()
        self.centralwidget_layout.addWidget(self.btn_1)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()