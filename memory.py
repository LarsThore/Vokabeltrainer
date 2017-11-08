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
        self.view.add_cards(self.cards)

        self.view.setMouseTracking(True)

    def set_layout(self):

        geometry = self.geometry

        self.layout = QGridLayout(self)

        self.scene = Scene(self)
        self.scene.setSceneRect(geometry.x(), geometry.y(), geometry.width(), geometry.height())
        self.scene.setBackgroundBrush(Qt.white)

        self.view = View()
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
                self.make_proxy(k, rect, voc[k])
                k += 1

    def make_proxy(self, k, rect, voc):

        label = QLabel('{}'.format(voc))
        label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        # create proxy
        proxy = Proxy()
        proxy.setWidget(label)
        proxy.setGeometry(rect)
        self.scene.addItem(proxy)

        # create parent grabby item, sized a bit bigger than proxy
        card = Card(k, rect, self.cards)
        card.setFlag(QGraphicsItem.ItemIsMovable, True)
        card.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.scene.addItem(card)
        self.cards.append(card)

        # set parent
        proxy.setParentItem(card)

class Scene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self)

    def mousePressEvent(self, event):
        QGraphicsScene.mousePressEvent(self, event)
        print(event.type())

        card_list = [item.parentItem() for item in self.items()]
        for card in card_list:
            if isinstance(card, Card):
                print(card.ID)
                print(card.boundingRect())

    def mouseReleaseEvent(self, event):
        QGraphicsScene.mouseReleaseEvent(self, event)
        print(event.type())

class View(QGraphicsView):

    def __init__(self, parent=None):
        QGraphicsView.__init__(self)

        self.cards = list()

    def add_cards(self, cards):
        self.cards = cards

    def event(self, event):
        QGraphicsView.event(self, event)
        # print(event)
        return True

    def mouseMoveEvent(self, event):
        QGraphicsView.mouseMoveEvent(self, event)

        for card in self.cards:
            print(card.ID)
            rect = card.boundingRect()
            if rect.contains(QMouseEvent.globalPos(event)):
                print('inside')
            else:
                print('outside')

        # print(QMouseEvent.globalPos(event))

class Proxy(QGraphicsProxyWidget):

    def __init__(self, parent=None):
        QGraphicsProxyWidget.__init__(self)

    def focusInEvent(self, event):
        self.parentItem().raise_zValue()

    # def event(self, event):
    #     QGraphicsProxyWidget.event(self, event)
    #     print(event.type())
    #     return True
    #
    # def ungrabMouseEvent(self, event):
    #     # QGraphicsProxyWidget.mouseReleaseEvent(self, event)
    #     print(event.type())
    #     # return True

class Card(QGraphicsRectItem):

    def __init__(self, ID, rect, cards, parent=None):
        QGraphicsRectItem.__init__(self, rect, parent=parent)

        self.cards = cards
        self.ID = ID

    def raise_zValue(self):
        z = [ item.zValue() for item in self.cards ]
        self.setZValue(max(z) + 0.1)

    def go_back(self):
        self.set.position(init_pos[0], init_pos[1])

    # def event(self, event):
    #     QGraphicsRectItem.event(self, event)
    #     print(event)
    #     return True

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
