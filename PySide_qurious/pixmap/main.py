# pylint: disable-msg=E0611
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

# Run MyApp
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):      
        pixmap = QPixmap()
        pixmap.load('C:/pywork/anything/PySide_qurious/pixmap/abc.png')
        pixmap = pixmap.scaledToWidth(1200)     
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        # lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        # lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        # vbox.addWidget(lbl_size)
        self.setLayout(vbox)

        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle('QPixmap')
        self.move(800, 300)
        
        self.ui = MyApp()
        self.setCentralWidget(self.ui)
        

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow() 
    window.show()
    app.exec()
    

    