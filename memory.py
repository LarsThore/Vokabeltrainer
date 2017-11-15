#! -*- coding:utf8 -*- #

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy
import sys

dummy_dict = {'sea':'Meer', 'ocean':'Ozean', 'harbour':'Hafen',
              'sea gull':'Möwe', 'boat':'Boot', 'shell':'Muschel',
              'to sail':'segeln', 'wave':'Welle'}

class Memory(QWidget):

    grid = None
    scene = None

    def __init__(self, geometry, vocabs=dummy_dict, parent=None):
        super(Memory, self).__init__(parent=parent)

        self.geometry = geometry
        self.vocabs = vocabs

        self.set_layout()
        self.cards = list()
        self.labels = list()
        self.add_cards()
        self.view.add_cards(self.cards)

        self.view.setMouseTracking(True)

        [label.add_dict(self.vocabs) for label in self.labels]

    def set_layout(self):

        geometry = self.geometry

        self.layout = QGridLayout(self)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(geometry.x(), geometry.y(), geometry.width(), geometry.height())
        self.scene.setBackgroundBrush(Qt.white)

        self.view = View()
        self.view.setScene(self.scene)

        self.layout.addWidget(self.view)

    def add_cards(self):

        voc = list(numpy.random.choice(list(self.vocabs.keys()), size = 8, replace = False))
        vocb = voc[:]

        if len(list(self.vocabs.keys())) == 8:
            for v in vocb:
                voc.append(self.vocabs[v])
        else:
            for v in vocb:
                voc.append(self.vocabs[v][0])

        numpy.random.shuffle(voc)

        w = 200
        h = 100

        x_offset = 100
        y_offset = 90

        k = 0

        for i in range(4):
            x = i*w
            for j in range(4):
                y = j*h
                rect = QRectF(x + x_offset + i*30, y + y_offset + j*40, w, h)
                self.make_proxy(k, rect, voc[k])
                k += 1

    def make_proxy(self, k, rect, voc):

        label = Label('{}'.format(voc))
        label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.labels.append(label)

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

class View(QGraphicsView):

    def __init__(self, parent=None):
        QGraphicsView.__init__(self)

        self.cards = list()

    def add_cards(self, cards):

        self.cards = cards

    def mouseReleaseEvent(self, event):
        QGraphicsView.mouseReleaseEvent(self, event)

        items = self.items(event.pos())

        i = 0
        if len(items) > 2:
            for item in items:
                if isinstance(item, Proxy):
                    print(item)
                    if i == 0:
                        item0 = item.widget()
                        text = item0.text()
                        i += 1
                    else:
                        if item.widget().releaseAction(text):
                            item0.change_style_green()

class Label(QLabel):

    def __init__(self, string, parent=None):
        QLabel.__init__(self, string, parent=parent)

        self.setStyleSheet("QLabel { background-color : lightgray }")
        self.dict = dict()

    def add_dict(self, dict_):

        self.dict = dict_

    def change_style_green(self):

        self.setStyleSheet("QLabel { background-color : green }")
        self.update()

    def releaseAction(self, text):

        if self.dict.get(text) == self.text() or self.dict.get(self.text()) == text:
            self.change_style_green()
            return True
        else:
            return False

class Proxy(QGraphicsProxyWidget):

    def __init__(self, parent=None):
        QGraphicsProxyWidget.__init__(self)

    def focusInEvent(self, event):
        self.parentItem().raise_zValue()

class Card(QGraphicsRectItem):

    def __init__(self, ID, rect, cards, parent=None):
        QGraphicsRectItem.__init__(self, rect, parent=parent)

        self.ID = ID
        self.cards = cards

    def raise_zValue(self):
        z = [ item.zValue() for item in self.cards ]
        self.setZValue(max(z) + 0.1)

    def go_back(self):
        self.set.position(init_pos[0], init_pos[1])



# print all methods
# method_list = [func for func in dir(QLabel) if not func.startswith("__")]
# for method in method_list:
#     print(method)

def main():

    app = QApplication(sys.argv)
    form = Memory(QRect(10, 10, 1065, 685))

    # place application in screen center
    screenGeometry = QApplication.desktop().screenGeometry()
    x = (screenGeometry.width()-form.width()) / 2
    y = (screenGeometry.height()-form.height()) / 2
    form.move(x, y)

    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
