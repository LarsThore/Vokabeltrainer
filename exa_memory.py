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

        self.geometry = geometry
        self.set_layout()
        self.cards = list()

        rect = QRectF(30, 40, 60, 60)

        card = Card(rect)
        self.scene.addItem(card)
        self.cards.append(card)

    def set_layout(self):

        geometry = self.geometry

        self.layout = QGridLayout(self)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(geometry.x(), geometry.y(), geometry.width(), geometry.height())
        self.scene.setBackgroundBrush(Qt.white)

        self.view = QGraphicsView()
        self.view.setScene(self.scene)

        self.layout.addWidget(self.view)


class Card(QGraphicsRectItem):

    def __init__(self, rect, parent=None):
        QGraphicsRectItem.__init__(self, rect, parent=parent)

        # self.brush().setColor(Qt.green)

def main():

    app = QApplication(sys.argv)
    form = Memory(QRect(10, 10, 200, 200))

    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


    # self.painter = QPainter()
    # self.brush = QBrush(Qt.green)
    # self.pen = QPen(Qt.gray)

    # def paint(self, painter, option, widget):
    #     painter.setBrush(self.brush)
    #     painter.setPen(self.pen)
    #     painter.drawRect(self.rectangle)


# print all methods
# method_list = [func for func in dir(RectItem) if not func.startswith("__")]
# for method in method_list:
#     print(method)
