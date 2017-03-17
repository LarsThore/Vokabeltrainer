#! -*- coding: utf-8 -*- #

from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtGui import QColor, QPen, QBrush, QCursor, QImage, QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

from types import MethodType
import sys
import numpy as np

app = QApplication(sys.argv)

##################### importing the file made qt designer #####################
w = loadUi("03-circles.ui")

#################### image for saving the picture of circles ##################
img = QImage(w.widget.width(), w.widget.height(), QImage.Format_RGB32)
img.fill(Qt.white)              # image appears white in the beginning (not black)

################################ set painter ##################################
imgPainter = QPainter()         # first painter
painter = QPainter()            # second painter

################################## set pen ####################################
line_drawer = QPen()
line_drawer.setWidth(4)

############################ set switch and lists #############################
switch = 0      # switch at 0 for first circle, at 1 for second circle

start_point_list = [0]
end_point_list = [0]
coordinate_set = set()

def draw_circles(x, y):
    print ( tuple((x, y)) ),

    imgPainter.begin(img)          # use first painter to draw on image
    imgPainter.setBrush(Qt.red)
    imgPainter.drawEllipse(x-10, y-10, 20, 20)    # draw circle (circles are represented as ellipse)
    imgPainter.end()


def fill_coordinate_set(x, y):
    for x_distance in range(-10, 11):            # set that will contain all pixels inside the circle
        for y_distance in range(-10, 11):        # (or still inside a square around the circle center)
            coordinate_set.add(tuple((x + x_distance, y + y_distance)))


def save_starting_point(event):
    '''
    saves the starting point of the line after a click on the widget
    '''

    start_point = event.pos()
    print ("start")
    start_point_list[0] = start_point


def draw_line(event):
    '''
    uses the starting point and the second point - which is indicated by
    another click - to draw a line between those points
    '''

    end_point = event.pos()
    print ("end")

    imgPainter.begin(img)          # use first painter to draw on image
    imgPainter.setPen(line_drawer)
    imgPainter.drawLine(start_point_list[0], end_point)    # draw line from first circle to second circle
    imgPainter.end()

def drawing(self, event):
    print (event.type())
    global switch

    print (event.type() == QEvent.MouseButtonPress and
            tuple((event.pos().x(), event.pos().y())) not in coordinate_set)

    if (event.type() == QEvent.MouseButtonPress and
        tuple((event.pos().x(), event.pos().y())) not in coordinate_set):  # recognize mouse click

        circle_center = event.pos()
        x = circle_center.x()
        y = circle_center.y()

        draw_circles(x, y)
        fill_coordinate_set(x, y)       # set value to dictionary key 'circle center'
        self.update()                   # requests a paint event


    elif (event.type() == QEvent.MouseButtonPress and switch == 0 and
            tuple((event.pos().x(), event.pos().y())) in coordinate_set):

        save_starting_point(event)
        switch = 1
        print ("switch: ", switch)

    elif (event.type() == QEvent.MouseButtonPress and switch == 1 and
            tuple((event.pos().x(), event.pos().y())) in coordinate_set):

        draw_line(event)
        self.update()                           # requests a paint event
        switch = 0
        print ("switch: ", switch)

    elif event.type() == QEvent.Paint:          # (you're only allowed to draw here (in a paint event) ?)
        painter.begin(self)                     # use second painter to draw image on widget
        painter.drawImage(0, 0, img)
        painter.end()

    return True                                 # ???


def erase():
    img.fill(Qt.white)
    #circles = ()         ############ TODO deleting circle list does not work ############
    w.widget.update()

w.widget.event = MethodType(drawing, w.widget)  # ersetzt die Funktion, die die Ereignisse behandelt ???
# w.eraseButton.clicked.connect(erase)

w.show()
sys.exit(app.exec_())
