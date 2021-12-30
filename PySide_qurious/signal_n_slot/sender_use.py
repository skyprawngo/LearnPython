from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class custom_btn(QPushButton):
    emit_btn_name = Signal(str)
    def __init__(
        self,
        i
    ):
        super().__init__()
        self.setObjectName(u"Button123")
        
        text = "btn_123: " + str(i)
        self.setObjectName(text)
        self.setText(text)
        self.emit_btn_name = self.text
        self.clicked.emit()
        
        

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
    
    def slot(self):
        button = self.sender()
        if button.objectName() == "btn_123: 0":
            print(button.text())
        if button.objectName() == "btn_123: 1":
            print(button.objectName())
        if button.objectName() == "btn_123: 2":
            print(button.objectName())
        if button.objectName() == "btn_123: 3":
            print(button.objectName())
        
        
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        for i in range(4):
            self.pushButton = custom_btn(
                i
            )
            self.pushButton.clicked.connect(self.slot)

            self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication()
    window = Ui_MainWindow() 
    window.show()
    app.exec()
    