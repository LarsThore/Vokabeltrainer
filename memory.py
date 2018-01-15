#! -*- coding:utf8 -*- #

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy
import sys

import time as clocktime

dummy_dict = {'sea':['Meer', 1], 'ocean':['Ozean', 1], 'harbour':['Hafen', 1],
              'sea gull':['Möwe', 1], 'boat':['Boot', 1], 'shell':['Muschel', 1],
              'to sail':['segeln', 1], 'wave':['Welle', 1]}

class Memory(QWidget):

    grid = None
    scene = None

    def __init__(self, geometry, app=None, vocabs=dummy_dict, parent=None):
        super(Memory, self).__init__(parent=parent)

        if app == None:
            self.app = self
        else:
            self.app = app

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

        self.view = View(self, self.scene)
        self.view.setScene(self.scene)

        self.layout.addWidget(self.view)

    def add_cards(self):

        keys = list(numpy.random.choice(list(self.vocabs.keys()), size = 8, replace = False))
        voc = keys[:]

        for key in keys:
            value_list = self.vocabs[key]
            for i in range(len(value_list)):
                if isinstance(value_list[i], str):
                    self.vocabs[key] = value_list[i]

        for key in keys:
            voc.append(self.vocabs[key])

        print(voc)

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
        label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
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

    def __init__(self, memory, scene, parent=None):
        QGraphicsView.__init__(self)

        self.memory = memory
        self.scene = scene

        self.cards = list()
        self.start_geometry = QRectF()

        self.pairs_found = 0

    def add_cards(self, cards):

        self.cards = cards

    def mousePressEvent(self, event):
        QGraphicsView.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        QGraphicsView.mouseReleaseEvent(self, event)

        items = self.items(event.pos())

        i = 0
        if len(items) > 2:
            for item in items:
                if isinstance(item, Proxy):
                    proxy = item
                    if i == 0:
                        proxy0 = proxy
                        label0 = proxy0.widget()
                        text0 = label0.text()
                        i += 1
                    else:
                        proxy1 = proxy
                        label1 = proxy1.widget()

                        def hide_all():
                            try:
                                label0.change_style_white()
                                label1.change_style_white()
                            except RuntimeError:
                                pass

                        if proxy1.widget().releaseAction(text0):
                            label0.change_style_green()
                            self.pairs_found += 1
                            QTimer.singleShot(300, hide_all)

                        else:
                            label0.change_style_red()

        if self.pairs_found == 8:
            self.scene.clear()
            self.memory.add_cards()
            # QTimer.singleShot(3000, self.scene.clear())
            # QTimer.singleShot(3000, self.memory.add_cards())
            self.pairs_found = 0


class Label(QLabel):

    def __init__(self, string, parent=None):
        QLabel.__init__(self, string, parent=parent)

        self.setStyleSheet("QLabel { background-color : lightgray }")
        self.dict = dict()

    def add_dict(self, dict_):

        self.dict = dict_

    def change_style_white(self):

        self.setStyleSheet("QLabel { background-color : White; color : lightGrey }")
        self.update()

    def change_style_green(self):

        self.setStyleSheet("QLabel { background-color : lightGreen }")
        self.update()

    def change_style_red(self):

        self.setStyleSheet("QLabel { background-color : IndianRed }")
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
        self.rect = rect
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
    form = Memory(QRect(10, 10, 1065, 685), app=app)

    # place application in screen center
    screenGeometry = QApplication.desktop().screenGeometry()
    x = (screenGeometry.width()-form.width()) / 2
    y = (screenGeometry.height()-form.height()) / 2
    form.move(x, y)

    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
