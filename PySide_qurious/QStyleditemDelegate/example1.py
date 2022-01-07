from PySide6 import QtCore, QtGui, QtWidgets


class MyStyledItem(QtWidgets.QStyledItemDelegate):
    def __init__(self, margin, radius, border_color, border_width, parent=None):
        """ 
        margin: distance between border and top of cell
        radius: radius of rounded corner
        border_color: color of border
        border_width: width of border
        """       
        super().__init__(parent)
        self.margin = margin
        self.radius = radius
        self.border_color = border_color
        self.border_width = border_width

    def sizeHint(self, option, index):
        # increase original sizeHint to accommodate space needed for border
        size = super().sizeHint(option, index)
        size = size.grownBy(QtCore.QMargins(0, self.margin, 0, self.margin))
        return size

    def paint(self, painter, option, index):
        painter.save()
        painter.setRenderHint(painter.Antialiasing)

        # set clipping rect of painter to avoid painting outside the borders
        painter.setClipping(True)
        painter.setClipRect(option.rect)
        
        # call original paint method where option.rect is adjusted to account for border
        option.rect.adjust(0, self.margin, 0, -self.margin)
        super().paint(painter, option, index)

        pen = painter.pen()
        pen.setColor(self.border_color)
        pen.setWidth(self.border_width)
        painter.setPen(pen)
        # draw either rounded rect for items in first or last column or ordinary rect
        if index.column() == 0:
            rect = option.rect.adjusted(self.border_width, 0, self.radius + self.border_width, 0)
            painter.drawRoundedRect(rect, self.radius, self.radius)
        elif index.column() == index.model().columnCount(index.parent()) - 1:
            rect = option.rect.adjusted(-self.radius-self.border_width, 0, -self.border_width, 0)
            painter.drawRoundedRect(rect, self.radius, self.radius)
        else:
            rect = option.rect.adjusted(-self.border_width, 0, self.border_width, 0)
            painter.drawRect(rect)
        # draw lines between columns
        if index.column() > 0:
            painter.drawLine(option.rect.topLeft(), option.rect.bottomLeft())
        painter.restore()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    # create test table
    table = QtWidgets.QTableWidget()
    table.resize(1000,600)
    table.setRowCount(3)
    table.setColumnCount(3)
    for row in range(table.rowCount()):
        for col in range(table.columnCount()):
            table.setItem(row, col, QtWidgets.QTableWidgetItem(f'item at {row=}, {col=}'))

    table.setShowGrid(False)
    delegate = MyStyledItem(margin=3, radius=10, border_width=2, border_color=QtGui.QColor("navy"))
    table.setItemDelegate(delegate)
    # the custom styled item delegate can be used with a style sheet
    table.setStyleSheet("QTableView::item {border: 0px; padding: 10px; }")
    # next line is needed to call the sizeHint of the item delegate
    table.resizeRowsToContents()
    table.show()
    app.exec()