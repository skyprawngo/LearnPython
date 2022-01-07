from PySide6 import QtWidgets
from PySide6.QtCore import SLOT,Slot

class NumberedButton(QtWidgets.QPushButton):

    def __init__(self, num):
        super().__init__()
        self.num = num
        self.setText(str(num))

    @Slot(int, str)
    def changeText(self, index, text):
        if index == self.num:
            self.setText(str(self.num) + text)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.cw = QtWidgets.QWidget()
        self.vb = QtWidgets.QVBoxLayout()
        self.c = QtWidgets.QComboBox()
        self.c.addItem('0')
        self.c.addItem('1')
        self.c.addItem('2')
        self.c.addItem('3')
        self.c.addItem('4')
        self.l = QtWidgets.QLineEdit()
        self.vb.addWidget(self.c)
        self.vb.addWidget(self.l)
        
        for i in range(5):
            btn = NumberedButton(i)
            self.vb.addWidget(btn)
            self.l.textChanged.connect(lambda text, btn=btn: btn.changeText(self.c.currentIndex(), text))

        self.cw.setLayout(self.vb)
        self.setCentralWidget(self.cw)

        self.c.currentIndexChanged.connect(lambda index: self.l.clear())

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = MainWindow()
    win.show()

    app.exec()