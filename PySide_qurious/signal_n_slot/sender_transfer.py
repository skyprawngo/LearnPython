from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class custom_widget(QWidget):
    def __init__(
        self,
    ):
        super().__init__()
        self.setup_Ui()
        pass
    
    def setup_Ui(self):
        self._layout = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setText("asd")
        self.label.setStyleSheet("background-color: darkgray;")
        self._layout.addWidget(self.label)
        
    
    def slot(self):
        self.label.setText(self.emit_information)
        print(self.emit_information2)
        
class custom_btn(QPushButton):
    signal = Signal()
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
        self.emit_information = text
        self.clicked.emit()
        self.pressed.connect(self.press_emit)
        
    def press_emit(self):
        emit_information2 = "aaaaa"
        self.signal.emit(self.emit_information, emit_information2)
        
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.label_widget = custom_widget()
        self.verticalLayout.addWidget(self.label_widget)
        
        for i in range(4):
            self.pushButton = custom_btn(
                i
            )
            self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)

if __name__ == "__main__":
    app = QApplication()
    window = Ui_MainWindow() 
    window.show()
    app.exec()
    