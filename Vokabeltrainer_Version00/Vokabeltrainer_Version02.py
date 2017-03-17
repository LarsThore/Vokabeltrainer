#! -*- coding: utf-8 -*- #

from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtGui import (QColor, QPen, QBrush, QCursor, QImage,
    QPainter, QTextCursor)
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

from types import MethodType
import sys
import numpy

# TODO: "Trotzdem Richtig" - Button einführen
# TODO: Vokabelliste in zweiten Tab einfügen
# TODO: Level richtig aktualisieren
# TODO: Level richtig speichern
# TODO: Funktion/Programm zum Importieren von Vokabellisten einfügen 

############################### load dictionary ###############################

french_german = {}

app = QApplication(sys.argv)

##################### importing the file made by qt designer ##################
widget = loadUi("vokabeln_gui00.ui")

################################# Functions ###################################

def import_data(input_file):
    '''
    Import whole vocabulary from 'Vocabulary.txt' into dictionary.

    Column 1: French
    Column 2: German
    Column 3: Level (1-5)
    '''
    with open (input_file, "r") as infile:
        for j, line in enumerate(infile):
            if j >= 1:
                try:
                    words = line.strip("\t")
                    word_list = words.split("\t")
                    level = word_list[2]
                    french_german[str(word_list[0])] = [word_list[1],
                                                            level.strip("\n")]
                except:
                    print ("Line not imported.")
                    continue

    print (french_german)

import_data("Vocabulary.txt")
############################# importing dictionary ############################

# make a list out of the keys of dictionary
french = list(french_german.keys())


def get_next_word():
    '''
    Chooses a word from the dictionary (keys) and writes it into the first
    line edit.
    '''
    # choose a random number to select a certain key from the dictionary
    e = numpy.random.randint(len(french_german))

    # fill the first text-edit-box with a word from the dictionary
    widget.lineEdit_1.setText(french[e])

    # set focus on second line edit
    widget.lineEdit_2.setFocus()

    return french[e]


def check_entry(word1, word2):
    '''
    Returns True if the word1 and word2 are a key-value-pair and False if not.
    '''

    word1 = str(word1[0])
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
widget.label_1.setText("   Französisch")
widget.label_2.setText("   Deutsch")

# write certain word into the first line edit field
word = get_next_word()

# after entering the word check (with function) if entry was correct
widget.lineEdit_2.returnPressed.connect(lambda:
    check_entry(french_german[widget.lineEdit_1.text()],
                widget.lineEdit_2.text()))



# start widget
widget.show()
sys.exit(app.exec_())
