from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class custom_label(QLabel):
    rainbow = ["red", "orange", "yellow", "lightgreen", "darkgreen", "blue", "navy","purple", "violet"]
    def __init__(
        self,
        number
        ):
        self.number = number
        super().__init__()
        self.setFixedSize(20, 15)
        self.setText(str(self.number))
    
    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.rainbow[self.number]))
        painter.drawEllipse(0, 0, 10, 10)
        painter.end()
        


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('drawEllipse')
        self.frame = QFrame()
        self.grid = QGridLayout(self.frame)
        for i in range(9):
            self.label = custom_label(i)
            self.grid.addWidget(self.label, 0, i)
        
        self.label1 = QLabel("asdf")
        self.grid.addWidget(self.label1)
        self.setCentralWidget(self.frame)
    
        
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    