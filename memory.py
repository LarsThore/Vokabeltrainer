#! -*- coding:utf8 -*- #

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Memory(QWidget):

    grid = None
    scene = None

    def __init__(self, geometry, parent=None):
        super(Memory, self).__init__(parent=parent)

        self.layout = QGridLayout(self)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(geometry.x(), geometry.y(), geometry.width(), geometry.height())
        self.scene.setBackgroundBrush(Qt.white)

        self.view = QGraphicsView()
        self.view.setScene(self.scene)

        self.layout.addWidget(self.view)

        self.cards = list()
        self.add_cards()

    def add_cards(self):

        w = 220
        h = 110

        for i in range(4):
            x = i*w
            for j in range(4):
                y = j*h
                rect = QRectF(x+35 + i*30, y+50 + j*40, w, h)
                self.make_proxy(rect)

    def make_proxy(self, rect):
        label = QLabel('Hallo')
        label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        # create my node
        proxy = QGraphicsProxyWidget()
        proxy.setWidget(label)
        proxy.setGeometry(rect)
        proxy.setFlag(QGraphicsItem.ItemStacksBehindParent, True)
        self.scene.addItem(proxy)
        # create parent grabby item, sized a bit bigger than proxy
        rectangle = QGraphicsRectItem(proxy.x(), proxy.y(),
        # rectangle = QGraphicsRectItem(100, 100,
                proxy.rect().width() + 1, proxy.rect().height() + 1)
        rectangle.setFlag(QGraphicsItem.ItemIsMovable, True)
        rectangle.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.scene.addItem(rectangle)
        # set parent
        proxy.setParentItem(rectangle)



# class Card(QGraphicsObject):
#
#     def __init__(self, text, rectangle, parent = None):
#         super(Card, self).__init__(parent=parent)
#
#         self.text = text
#
#         self.rectangle = rectangle
#
#         self.set_gradient(QColor(200, 200, 200, 170))
#         self.pen = QPen(Qt.NoPen)
#         self.brush = QBrush(self.gradient)
#
#         self.setFlag(QGraphicsItem.ItemIsMovable)
#
#     def boundingRect(self):
#         return self.rectangle
#
#     def set_gradient(self, color):
#         """Sets the color gradient of the edge"""
#
#         self.gradient = QLinearGradient(self.rectangle.bottomLeft(),
#                                         self.rectangle.topRight())
#         self.gradient.setColorAt(0.7, color)
#         self.gradient.setColorAt(1, color.darker(20))
#
#         return self.gradient
#
#     def paint(self, painter, option, widget):
        # painter.setBrush(self.brush)
        # painter.setPen(self.pen)
        # painter.drawRoundedRect(self.rectangle, 8, 8)
        # painter.drawText(self.boundingRect(), self.text)

def main():

    app = QApplication(sys.argv)
    form = Memory(QRect(10, 10, 1051, 661))

    # place application in screen center
    screenGeometry = QApplication.desktop().screenGeometry()
    x = (screenGeometry.width()-form.width()) / 2
    y = (screenGeometry.height()-form.height()) / 2
    form.move(x, y)

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
