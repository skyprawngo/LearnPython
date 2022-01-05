import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Btn_Push(QPushButton):
    clicked = Signal(object)
    def __init__(self):
        super().__init__()
        self.setText("쓰레드 실행 버튼")
        self.mythread = MyThread(self)
        self.clicked.connect(self.toggle)
        pass
    
    def toggle(self):
        if not self.mythread.func_run:
            self.mythread.func_run = True
            self.mythread.run()
        elif self.mythread.func_run:
            self.mythread.func_run = False
            
    pass
class MyThread(QThread):
    signal = Signal()
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.func_run = False
        pass

    def run(self):
        self.check = 0
        print(self.func_run)
        while self.func_run == True:
            if self.check >= 5:
                break
            print("진행중!")
            time.sleep(1) 
            self.check += 1
    pass
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.Frame = QFrame()
        self.Frame.setStyleSheet("background-color: darkgray;")
        self.vlayout = QVBoxLayout(self.Frame)
        self.btn_push = Btn_Push()
        self.vlayout.addWidget(self.btn_push)
        self.btn_1 = QPushButton("가짜 버튼")
        self.vlayout.addWidget(self.btn_1)
        self.setCentralWidget(self.Frame)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()