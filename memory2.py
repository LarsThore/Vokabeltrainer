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

        x_offset = 50
        y_offset = 30

        rect = QRectF(x_offset, y_offset, w, h)
        self.make_proxy(0, rect, voc[0])

    def make_proxy(self, k, rect, voc):

        label = Label('{}'.format(voc))
        label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.labels.append(label)

        # create proxy
        proxy = Proxy()
        proxy.setWidget(label)
        proxy.setGeometry(rect)
        self.scene.addItem(proxy)

        # create parent grab item, sized a bit bigger than proxy
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
        self.start_geometry = QRectF()

    def add_cards(self, cards):

        self.cards = cards

    def mousePressEvent(self, event):
        QGraphicsView.mousePressEvent(self, event)

        print('somthing')

        items = self.items(event.pos())

        for item in items:
            if isinstance(item, Proxy):
                self.start_geometry = item.geometry()


    def mouseReleaseEvent(self, event):
        QGraphicsView.mouseReleaseEvent(self, event)

        items = self.items(event.pos())
        # for function in dir(items[0]):
        #     if 'set' in function:
        #         print (function)


        for item in items:
            if isinstance(item, Proxy):
                proxy = item
                if i == 0:
                    label0 = proxy.widget()
                    text0 = label0.text()
                    proxy0 = proxy
                    # print(label0)
                    i += 1
                else:
                    proxy1 = proxy
                    label1 = proxy1.widget()
                    # print(label1)
                    print('1', proxy1.widget())
                    if proxy1.widget().releaseAction(text0):
                        label0.change_style_green()
                    else:
                        label0.change_style_red()
                        proxy0.setGeometry(self.start_geometry)
                        proxy0.widget().setGeometry(int(self.start_geometry.x()),
                                                  int(self.start_geometry.y()),
                                                  int(self.start_geometry.width()),
                                                  int(self.start_geometry.height()))

class Label(QLabel):

    def __init__(self, string, parent=None):
        QLabel.__init__(self, string, parent=parent)

        self.setStyleSheet("QLabel { background-color : lightgray }")
        self.dict = dict()

    def add_dict(self, dict_):

        self.dict = dict_

    def change_style_green(self):

        self.setStyleSheet("QLabel { background-color : lightGreen }")
        self.update()

    def change_style_red(self):

        self.setStyleSheet("QLabel { background-color : Red }")
        self.update()

    def releaseAction(self, text):

        if self.dict.get(text) == self.text() or self.dict.get(self.text()) == text:
            self.change_style_green()
            return True
        else:
            self.change_style_red()
            return False

class Proxy(QGraphicsProxyWidget):

    def __init__(self, parent=None):
        QGraphicsProxyWidget.__init__(self)

    def focusInEvent(self, event):
        self.parentItem().raise_zValue()

    def go_back(self):
        pass

class Card(QGraphicsRectItem):

    def __init__(self, ID, rect, cards, parent=None):
        QGraphicsRectItem.__init__(self, rect, parent=parent)

        self.ID = ID
        self.cards = cards

    def raise_zValue(self):
        z = [ item.zValue() for item in self.cards ]
        self.setZValue(max(z) + 0.1)

    def go_back(self):
        self.set_position(init_pos[0], init_pos[1])



# print all methods
# method_list = [func for func in dir(QLabel) if not func.startswith("__")]
# for method in method_list:
#     print(method)

def main():

    app = QApplication(sys.argv)
    form = Memory(QRect(10, 10, 450, 350))

    # place application in screen center
    screenGeometry = QApplication.desktop().screenGeometry()
    x = (screenGeometry.width()-form.width()) / 2
    y = (screenGeometry.height()-form.height()) / 2
    form.move(x, y)

    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
