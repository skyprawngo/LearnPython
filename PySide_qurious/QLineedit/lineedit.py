import sys
from PySide6.QtWidgets import *


class WindowClass(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi()

        #버튼에 기능을 할당하는 코드
        self.lineedit_Test.textChanged.connect(self.lineeditTextFunction)
        self.lineedit_Test.returnPressed.connect(self.printTextFunction)
        self.btn_changeText.clicked.connect(self.changeTextFunction)

    def lineeditTextFunction(self) :
        self.lbl_textHere.setText(self.lineedit_Test.text())

    def printTextFunction(self) :
        #self.lineedit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        print(self.lineedit_Test.text())

    def changeTextFunction(self) :
        #self.lineedit이름.setText("String")
        #Lineedit의 글자를 바꾸는 메서드
        self.lineedit_Test.setText("Change Text")
    
    def setupUi(self):
        self.resize(800, 600)
        self.frame1 = QFrame()
        self.layout1 = QVBoxLayout(self.frame1)

        self.lbl_textHere = QLabel()
        self.layout1.addWidget(self.lbl_textHere)

        self.lineedit_Test = QLineEdit()
        self.layout1.addWidget(self.lineedit_Test)
        
        self.btn_changeText = QPushButton("change")
        self.layout1.addWidget(self.btn_changeText)

        self.setCentralWidget(self.frame1)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()