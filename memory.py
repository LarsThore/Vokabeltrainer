#! -*- coding:utf8 -*- #

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy
import sys

class Memory(QWidget):

    grid = None
    scene = None

    def __init__(self, geometry, vocabs, parent=None):
        super(Memory, self).__init__(parent=parent)

        self.geometry = geometry
        self.vocabs = vocabs

        self.set_layout()
        self.cards = list()
        self.add_cards()

    def set_layout(self):

        geometry = self.geometry

        self.layout = QGridLayout(self)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(geometry.x(), geometry.y(), geometry.width(), geometry.height())
        self.scene.setBackgroundBrush(Qt.white)

        self.view = QGraphicsView()
        self.view.setScene(self.scene)

        self.layout.addWidget(self.view)

    def add_cards(self):

        voc = list(numpy.random.choice(list(self.vocabs.keys()), size = 8, replace = False))
        vocb = voc[:]

        for v in vocb:
            voc.append(self.vocabs[v][0])

        numpy.random.shuffle(voc)

        w = 200
        h = 100

        k = 0

        for i in range(4):
            x = i*w
            for j in range(4):
                y = j*h
                rect = QRectF(x+15 + i*30, y+30 + j*40, w, h)
                self.make_proxy(rect, voc[k])
                k += 1

    def make_proxy(self, rect, voc):

        label = QLabel('{}'.format(voc))
        label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        # create proxy
        proxy = Proxy()
        proxy.setWidget(label)
        proxy.setGeometry(rect)
        self.scene.addItem(proxy)

        # create parent grabby item, sized a bit bigger than proxy
        card = RectItem(rect, self.cards)
        card.setFlag(QGraphicsItem.ItemIsMovable, True)
        card.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.scene.addItem(card)
        self.cards.append(card)

        # set parent
        proxy.setParentItem(card)


class Proxy(QGraphicsProxyWidget):

    def __init__(self, parent=None):
        QGraphicsProxyWidget.__init__(self)

    def focusInEvent(self, event):
        self.parentItem().raise_zValue()

class RectItem(QGraphicsRectItem):

    def __init__(self, rect, cards, parent=None):
        QGraphicsRectItem.__init__(self, rect, parent=parent)
        self.cards = cards

    def raise_zValue(self):
        z = [ item.zValue() for item in self.cards ]
        self.setZValue(max(z) + 0.1)

def main():

    app = QApplication(sys.argv)
    form = Memory(QRect(10, 10, 900, 550))

    # place application in screen center
    screenGeometry = QApplication.desktop().screenGeometry()
    x = (screenGeometry.width()-form.width()) / 2
    y = (screenGeometry.height()-form.height()) / 2
    form.move(x, y)

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

'''
Probably this is because the flag is a convenience function that uses the
original `boundingRect` method of the `QGraphicsRectItem` class and since I
redefine this function the behavior is faulty.
'''


# print all methods
# method_list = [func for func in dir(RectItem) if not func.startswith("__")]
# for method in method_list:
#     print(method)
