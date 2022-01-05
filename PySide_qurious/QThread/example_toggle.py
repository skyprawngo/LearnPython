import sys, time
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MyThread(QThread):
        def __init__(self, parent = None):
                QThread.__init__(self, parent)
                self.exiting = False

        def run(self):
                while self.exiting==False:
                        sys.stdout.write('.')
                        sys.stdout.flush()
                        time.sleep(1)

class MainWindow(QMainWindow):
        def __init__(self, parent=None):
                QMainWindow.__init__(self,parent)
                self.centralwidget = QWidget(self)
                self.batchbutton = QPushButton('Start batch',self)
                self.label1 = QLabel('Continuos batch')
                self.label2 = QLabel('Long batch')
                self.vbox = QVBoxLayout()
                self.vbox.addWidget(self.batchbutton)
                self.vbox.addWidget(self.label1)
                self.vbox.addWidget(self.label2)
                self.setCentralWidget(self.centralwidget)
                self.centralwidget.setLayout(self.vbox)
                self._thread = MyThread()
                self.batchbutton.clicked.connect(self.handletoggle)
                self._thread.started.connect(self.started)
                self._thread.finished.connect(self.finished)

        def started(self):
                self.label1.setText('Continuous batch started')

        def finished(self):
                self.label1.setText('Continuous batch stopped')

        def terminated(self):
                self.label1.setText('Continuous batch terminated')

        def handletoggle(self):
                if self._thread.isRunning():
                        self._thread.exiting=True
                        self.batchbutton.setEnabled(False)
                        while self._thread.isRunning():
                                time.sleep(0.01)
                                continue
                        self.batchbutton.setText('Start batch')
                        self.batchbutton.setEnabled(True)
                else:
                        self._thread.exiting=False
                        self._thread.start()
                        self.batchbutton.setEnabled(False)
                        while not self._thread.isRunning():
                                time.sleep(0.01)
                                continue
                        self.batchbutton.setText('Stop batch')
                        self.batchbutton.setEnabled(True)

if __name__=='__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec()