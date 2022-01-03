#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
 
 
class Second(QMainWindow):
    def __init__(self, parent):
        self._parent = parent
        super(Second, self).__init__(parent)
        self.pushButton2 = QPushButton("click me2")
        self.setCentralWidget(self.pushButton2)
        self.pushButton2.clicked.connect(self.off_pushButton_clicked)
    
    def off_pushButton_clicked(self):
        self.hide()
        self._parent.show()
 
 
class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.pushButton = QPushButton("click me")
 
        self.setCentralWidget(self.pushButton)
 
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)
        
 
    def on_pushButton_clicked(self):
        self.hide()
        self.dialog.show()
        
 
 
def main():
    app = QApplication(sys.argv)
    main = First()
    main.show()
    app.exec()
 
if __name__ == '__main__':
    main()