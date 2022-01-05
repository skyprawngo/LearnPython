import sys, time
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MyLongThread(QThread):
    signal = Signal(str)
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False

    def run(self):
        end = time.time()+5
        while self.exiting==False:
            sys.stdout.write('*')
            sys.stdout.flush()
            time.sleep(1)
            now = time.time()
            if now>=end:
                    self.exiting=True
        self.signal.emit('OK')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.centralwidget = QWidget(self)
        self.longbutton = QPushButton('Start long (5 seconds) operation',self)
        self.label1 = QLabel('Continuos batch')
        self.label2 = QLabel('Long batch')
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.longbutton)
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(self.vbox)
        self.longthread = MyLongThread()
        self.longbutton.clicked.connect(self.longoperation)
        self.longthread.signal.connect(self.longoperationcomplete)

    def longoperation(self):
        if not self.longthread.isRunning():
            self.longthread.exiting=False
            self.longthread.start()
            self.label2.setText('Long operation started')
            self.longbutton.setEnabled(False)

    def longoperationcomplete(self,data):
        self.label2.setText('Long operation completed with: '+data)
        self.longbutton.setEnabled(True)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()