import sys, time
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class custom_label(QLabel):
    def __init__(self):
        super().__init__()
        self.setup_Ui()
    
    def setup_Ui(self):
        self._layout = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setText("custom_label")
        self._layout.addWidget(self.label)
        
        # MyLongThread에서 run 작동이 끝나서 발송한 emit에서
        # MainWindow를 거치지 않고 information인 "OK"를
        # custom_label에서 setText로 출력하는 방법 
        self.connect

    def slot(self):
        self.label.setText(self.information)


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
        self.signal.emit(information = 'OK')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.centralwidget = QWidget(self)
        self.longbutton = QPushButton('Start long (5 seconds) operation',self)
        self.label1 = QLabel('Continuos batch')
        self.label2 = QLabel('Long batch')
        self.label3 = custom_label()
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