import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        layout = QVBoxLayout(self)

        self.viewer = NodeGraph(self)
        layout.addWidget(self.viewer)

class NodeGraph(QGraphicsView):
    def __init__(self, parent):
        super(NodeGraph, self).__init__(parent)

        self._scene = QGraphicsScene(self)
        self.CreatePicNode()
        
        self.setGeometry(100, 100, 200, 200)

        self.setScene(self._scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setBackgroundBrush(QBrush(QColor(30, 30, 30)))
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.RubberBandDrag)

    def CreatePicNode(self):
        # create my node
        nodeProxy = QGraphicsProxyWidget()
        nodeProxy.setWidget(QLabel('Hallo'))
        nodeProxy.setFlag(QGraphicsItem.ItemStacksBehindParent, True)
        self._scene.addItem(nodeProxy)
        # create parent grabby item, sized a bit bigger than nodeProxy
        item1 = QGraphicsRectItem(-1, -1, nodeProxy.rect().width() + 1, nodeProxy.rect().height() + 1)
        item1.setFlag(QGraphicsItem.ItemIsMovable, True)
        item1.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self._scene.addItem(item1)
        # set parent
        nodeProxy.setParentItem(item1)

def main():
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
