import os
from PySide6 import QtCore, QtGui, QtWidgets

class PushButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super(PushButton, self).__init__(*args, **kwargs)
        self.setStyleSheet('''background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fdfbf7, stop: 1 #6190F2);
            border-style: solid;border-width: 2px;
            border-radius: 8px;
            border-color: #9BB7F0;padding: 3px;''')

        icon = self.icon()
        icon_size = self.iconSize()
        # remove icon
        self.setIcon(QtGui.QIcon())
        label_icon = QtWidgets.QLabel()
        label_icon.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        label_icon.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        lay = QtWidgets.QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(label_icon, alignment=QtCore.Qt.AlignRight)
        label_icon.setPixmap(icon.pixmap(icon_size))

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        icon = QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_ArrowRight)
        # icon = QtGui.QIcon(os.path.join('logo_png_apsc', 'icone_3_fleches_droite_apsc_256x256.png'))

        bout_pag_charg_enr_phase_1 = PushButton("Aller directement à la page de maintenance de la Séquence",
            icon=icon, iconSize=QtCore.QSize(16, 16))
        bout_pag_charg_enr_phase_1.setFixedWidth(506)

        bout_pag_suivante_phase_1 = PushButton("Page suivante",
            icon=icon, iconSize=QtCore.QSize(16, 16))
        bout_pag_suivante_phase_1.setFixedWidth(140)

        lay = QtWidgets.QHBoxLayout(self)
        lay.addWidget(bout_pag_charg_enr_phase_1)
        lay.addWidget(bout_pag_suivante_phase_1)        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())