#! -*- coding: utf-8 -*- #

from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtGui import (QColor, QPen, QBrush, QCursor, QImage,
    QPainter, QTextCursor)
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

from types import MethodType
import sys
import numpy

############################### load dictionary ###############################

german_french = {"Haus" : "la maison",
                 "Mutter" : "la mere",
                 "Ziel" : "le destination",
                 "Glas" : "la verre",
                 "letzte" : "dernier",
                 }

app = QApplication(sys.argv)

##################### importing the file made by qt designer ##################
widget = loadUi("vokabeln_gui00.ui")

################################# Functions ###################################

def import_data(input_file):
    '''
    Import whole vocabulary from 'Vocabulary.txt' into dictionary.

    Column 1: German
    Column 2: French
    Column 3: Level (1-5)
    '''
    with open (input_file, "r") as infile:
        for j, line in enumerate(infile):
            if j >= 1:
                words = line.strip("\t")
                word_list = words.split("\t")
                german_french[str(word_list[0])] = word_list[1]

    print (german_french)

import_data("Vocabulary.txt")
############################# importing dictionary ############################

# make a list out of the keys of dictionary
german = list(german_french.keys())


def get_next_word():
    '''
    Chooses a word from the dictionary (keys) and writes it into the first
    line edit.
    '''
    # choose a random number to select a certain key from the dictionary
    e = numpy.random.randint(len(german_french))

    # fill the first text-edit-box with a word from the dictionary
    widget.lineEdit_1.setText(german[e])

    # set focus on second line edit
    widget.lineEdit_2.setFocus()

    return german[e]


def check_entry(word1, word2):
    '''
    Returns True if the word1 and word2 are a key-value-pair and False if not.
    '''

    word1 = str(word1)
    word2 = str(word2)

    print(word1, word2)

    if word1 == word2:
        print (True)
        widget.label.setText("Richtig!")
        get_next_word()
        widget.lineEdit_2.clear()
        widget.lineEdit_2.setFocus()
    else:
        print (False)
        widget.label.setText("Leider Falsch!")



# set text of text labels for language 1 and language 2
widget.label_1.setText("Deutsch")
widget.label_2.setText("Französisch")

# loop over all word pairs
# for i in range(len(german_french)):

# write certain word into the first line edit field
word = get_next_word()

# after entering the word check (with function) if entry was correct
widget.lineEdit_2.returnPressed.connect(lambda:
    check_entry(german_french[widget.lineEdit_1.text()],
                widget.lineEdit_2.text()))



# start widget
widget.show()
sys.exit(app.exec_())
