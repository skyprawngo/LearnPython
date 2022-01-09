from PySide6 import QtWidgets
from PySide6.QtCore import QLocale, QObject, Qt, Signal, Slot
from PySide6.QtGui import QInputMethodEvent

class NumberedButton(QtWidgets.QPushButton):
    sig = Signal(str)

    def __init__(self, num):
        super().__init__()
        self.num = num
        self.setText(str(num))

        self.clicked.connect(self.sendNum)

    def sendNum(self):
        self.sig.emit(str(self.num))
        print(str(self.num))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.cw = QtWidgets.QWidget()
        self.vb = QtWidgets.QVBoxLayout()
        self.l = QtWidgets.QLineEdit()
        self.vb.addWidget(self.l)
        
        for i in range(5):
            btn = NumberedButton(i)
            self.vb.addWidget(btn)

            btn.sig.connect(self.l.setText)

        self.cw.setLayout(self.vb)
        self.setCentralWidget(self.cw)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = MainWindow()
    win.show()

    app.exec()

