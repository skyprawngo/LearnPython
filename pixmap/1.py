# pylint: disable-msg=E0611
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap

# Run MyApp
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):      
        pixmap = QPixmap()
        pixmap.load('C:/pywork/anything/pixmap/abc.png')
        pixmap = pixmap.scaledToWidth(400)     
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        # lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        # lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        # vbox.addWidget(lbl_size)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(1500, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()
    