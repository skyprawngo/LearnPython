from PySide6 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.m_table = QtWidgets.QTableWidget(0, 1)
        self.m_table.verticalHeader().hide()
        self.m_table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.m_lineedit = QtWidgets.QLineEdit()
        self.left_button = QtWidgets.QPushButton(
            "Left", clicked=self.on_left_clicked
        )
        self.right_button = QtWidgets.QPushButton(
            "Right", clicked=self.on_right_clicked
        )

        lay = QtWidgets.QGridLayout(self)
        lay.addWidget(self.m_table, 0, 0, 1, 2)
        lay.addWidget(self.m_lineedit, 1, 0, 1, 2)
        lay.addWidget(self.left_button, 2, 0)
        lay.addWidget(self.right_button, 2, 1)

    def on_left_clicked(self):
        self.add_label(self.m_lineedit.text(), QtCore.Qt.AlignLeft)
        self.m_lineedit.clear()
        self.m_table.scrollToBottom()

    def on_right_clicked(self):
        self.add_label(self.m_lineedit.text(), QtCore.Qt.AlignRight)
        self.m_lineedit.clear()
        self.m_table.scrollToBottom()

    def add_label(self, text, alignment):
        label = QtWidgets.QLabel(text, alignment=alignment)
        row = self.m_table.rowCount()
        self.m_table.insertRow(row)
        self.m_table.setCellWidget(row, 0, label)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    app.exec()