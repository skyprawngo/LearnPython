import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *

class Btn_1(QPushButton):
    def __init__(
        self,
        parent,
        app_parent
    ):
        super().__init__()

        self.parent = parent
        self.app_parent = app_parent
        
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(50, 50)
        self.btn_image = QIcon()
        self.btn_image.addFile("QLabelemergeQurious/add.svg")
        self.setIcon(self.btn_image)
        self.setIconSize(QSize(50, 50))
        

        self.label_1 = pylabel(
            parent,
            tooltip_text = "asdasd",
            tooltip_text_color = "#fff000",
            tooltip_bg_color = "#000fff"

        )
        self.label_1.setFixedSize(100,50)
        self.label_1.setStyleSheet("background-color: lightblue;")
        self.label_1.hide()

        
    
    def enterEvent(self, event):
        self.move_tooltip()
        self.label_1.show()
        print("엔터이벤트")
    
    def leaveEvent(self, event):
        self.move_tooltip()
        self.label_1.hide()
        print("리브이벤트")
    
    def move_tooltip(self):
        gp = self.mapToGlobal(QPoint(0, 0))
        pos = self.mapFromGlobal(gp)

        pos_x = (pos.x() - self.label_1.width()) + self.width() + 5
        pos_y = pos.y() + self.height() + 6
        # SET POSITION TO WIDGET
        # Move tooltip position
        self.label_1.move(pos_x, pos_y)

class pylabel(QLabel):
    style_tooltip = """ 
    QLabel {{		
        background-color: darkgray;	
        color: {tooltip_text_color};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
    }}
    """  

    def __init__(
        self,
        parent,
        tooltip_text,
        tooltip_text_color,
        tooltip_bg_color
    ):

        QLabel.__init__(self)
        # LABEL SETUP
        style = self.style_tooltip.format(
            tooltip_bg_color = tooltip_bg_color,
            tooltip_text_color = tooltip_text_color
        )

        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(34)
        self.setParent(parent)
        self.setText(tooltip_text)
        self.adjustSize()

        print(self.adjustSize())

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)