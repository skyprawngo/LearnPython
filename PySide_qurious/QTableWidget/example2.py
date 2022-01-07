import  sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PaintTable(QTableWidget):
    def __init__(self, parent):
        QTableWidget.__init__(self, parent)
        self.setRowCount(10) 
        self.setColumnCount(10)
        self.center = QPoint(-10,-10)

    def paintEvent(self, event):
        painter = QPainter(self.viewport()) #See: http://stackoverflow.com/questions/12226930/overriding-qpaintevents-in-pyqt
        painter.drawEllipse(self.center,10,10)
        QTableWidget.paintEvent(self,event)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.RightButton:
            self.center = QPoint(event.pos().x(),  event.pos().y())
            print (self.center)
            self.viewport().repaint()

        elif event.buttons() == Qt.LeftButton:
            QTableWidget.mousePressEvent(self,event)


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.resize(1100, 400)

        self.table = PaintTable(self)
        self.setCentralWidget(self.table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    app.exec()