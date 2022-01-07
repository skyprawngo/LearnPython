import sys

#from PyQt4 import QtCore, QtGui 
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PaintTable(QTableWidget):
    def __init__(self, parent):
        QTableWidget.__init__(self, parent)
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

class MainWindow(PaintTable):
    def __init__(
        self,
        parent = None
    ):
        super(MainWindow, self).__init__(parent)

# General grid
        self.table = PaintTable(self)
        self.nbrow, self.nbcol = 9, 9
        self.table.setRowCount(self.nbrow)
        self.table.setColumnCount(self.nbcol)
        for row in range(0, self.nbrow):
            self.table.setRowHeight(row, 50)

            for col in range(0, self.nbcol):
                self.table.setColumnWidth(col, 50)

# Each cell contains one single QTableWidgetItem
        for row in range(0, self.nbrow):
            for col in range(0, self.nbcol):
                item = QTableWidgetItem()
                item.setTextAlignment(
                    Qt.AlignHCenter | Qt.AlignVCenter
                )

                self.table.setItem(row, col, item)

# Header formatting
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(12)
        self.table.horizontalHeader().setFont(font)
        self.table.verticalHeader().setFont(font)

# Font used
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(20)
        self.table.setFont(font)

# Global Size
        self.resize(60*9, 60*9 + 20)

# Layout of the table
        layout = QGridLayout()
        layout.addWidget(self.table, 0, 0)
        self.setLayout(layout)

# Set the focus in the first cell
        self.table.setFocus()
        self.table.setCurrentCell(0, 0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = MainWindow()
    fen.show()
    app.exec()