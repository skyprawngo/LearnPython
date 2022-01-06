from PySide6 import QtWidgets
from PySide6.QtCore import QLocale, QObject, Qt, Signal, Slot
from PySide6.QtGui import QInputMethodEvent

class Custom_label(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        self._parent = parent
        self._layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel()
        self._parent.btn.sig.connect(self.slot)
        self._layout.addWidget(self.label)
    
    def slot(self):
        print("aaaa")

class NumberedButton(QtWidgets.QPushButton):
    sig = Signal(str)

    def __init__(self, num):
        super().__init__()
        self.num = num
        self.setText(str(num))

        self.clicked.connect(self.sendNum)

    def sendNum(self):
        self.sig.emit(str(self.num))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.cw = QtWidgets.QWidget()
        self.vb = QtWidgets.QVBoxLayout()
        self.l = QtWidgets.QLineEdit()
        self.vb.addWidget(self.l)
        
        self.l2 = Custom_label(parent=self)
        self.vb.addWidget(self.l2)
        
        for i in range(5):
            self.btn = NumberedButton(i)
            self.vb.addWidget(self.btn)

            self.btn.sig.connect(self.l.setText)

        self.cw.setLayout(self.vb)
        self.setCentralWidget(self.cw)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = MainWindow()
    win.show()

    app.exec()

