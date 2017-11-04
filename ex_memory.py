#! -*- coding:utf8 -*- #

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Memory(QWidget):

    grid = None
    scene = None

    def __init__(self, parent=None):
        super(Memory, self).__init__(parent=parent)

        self.layout = QGridLayout(self)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(10, 10, 400, 400)
        self.scene.setBackgroundBrush(Qt.white)

        self.view = QGraphicsView()
        self.view.setScene(self.scene)

        self.layout.addWidget(self.view)

        self.cards = list()
        self.add_items()

    def add_items(self):

        item = TextItem('Hallo')
        self.cards.append(item)
        self.scene.addItem(item)

class TextItem(QGraphicsTextItem):

    def __init__(self, text):
        QGraphicsTextItem.__init__(self, text)
        self.text=text
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

    def boundingRect(self):
        return QRectF(150, 150, 100, 100)

    def paint(self, painter, option, widget):
        self.pen = QPen()
        self.pen.setWidth(2)
        painter.setPen(self.pen)
        painter.drawRect(self.boundingRect())
        painter.drawText(self.boundingRect(),self.text)

# class Card(QGraphicsRectItem):
# class Card(QGraphicsTextItem):
class Card(QGraphicsSimpleTextItem):
# class Card(QGraphicsObject):

    def __init__(self, parent = None):
        super(Card, self).__init__(parent=parent)

        self.pen = QPen(Qt.black)
        self.brush = QBrush(Qt.white)
        # self.setFlag(QGraphicsItem.ItemIsMovable)

        # self.setPlainText('Hello')
        self.setText('Hello')

    def boundingRect(self):
        return QRectF(150, 150, 100, 100)

    def paint(self, painter, option, widget):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawRoundedRect(QRectF(150, 150, 100, 100), 10, 10)

def main():

    app = QApplication(sys.argv)
    form = Memory()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
