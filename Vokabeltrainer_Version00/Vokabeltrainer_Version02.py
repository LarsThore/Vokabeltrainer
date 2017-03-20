#! -*- coding: utf-8 -*- #

from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtGui import (QColor, QPen, QBrush, QCursor, QImage,
    QPainter, QTextCursor, QKeySequence)
from PyQt5.QtWidgets import QWidget, QApplication, QShortcut
from PyQt5.uic import loadUi

from types import MethodType
import sys
import numpy

# TODO: "Trotzdem Richtig" - Button einführen
# TODO: Vokabelliste in zweiten Tab einfügen
# TODO: Level richtig aktualisieren
#           - bei richtigen Antworten    -----   DONE
#           - bei falschen Antworten    ----- Do Nothing
# TODO: Level richtig speichern
# TODO: Tooltipps einfügen
# TODO: mehr Wörter der unteren Level auswählen
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

    for entry in french_german:
        print (entry) 

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

    # show the level value
    values = french_german[french[e]]
    level_text = str(values[1])
    widget.label_level.setText(level_text)

    # set focus on second line edit
    widget.lineEdit_2.setFocus()

    return french[e]


def check_entry(word1, word2, word3):
    '''
    Returns True if the word1 and word2 are a key-value-pair and False if not.
    '''
    # extract correct word from the list in dictionary according to
    # first line edit -- second language -- correct word
    word1 = str(word1[0])
    # the word in second line edit -- second language -- tested word
    word2 = str(word2)
    # the respective word in - first language
    word3 = str(word3)

    print(word1, word2)

    if word1 == word2:
        print (True)
        widget.label.setText("Richtig!")
        get_next_word()

        # Textfelder neu einrichten
        widget.lineEdit_2.clear()
        widget.lineEdit_2.setFocus()

        # Level aktualisieren
        values = french_german[word3]
        level = int(values[1])
        french_german[word3] = [word2, level + 1]
        return True
    else:
        print (False)
        widget.label.setText("Leider Falsch!")
        widget.lineEdit_2.setFocus()
        widget.lineEdit_2.selectAll()
        return False


# set text of text labels for language 1 and language 2
widget.label_1.setText("   Französisch")
widget.label_2.setText("   Deutsch")

# write certain word into the first line edit field
word = get_next_word()

# after entering the word check (with function) if entry was correct
answer = widget.lineEdit_2.returnPressed.connect(lambda:
    check_entry(french_german[widget.lineEdit_1.text()],
                widget.lineEdit_2.text(), widget.lineEdit_1.text()))

if answer == True:
    pass
else:
    if widget.pushButton.clicked or widget.pushButton.returnPressed:
        widget.pushButton.clicked.connect(get_next_word)


# close the widget with shortcut (ESCAPE KEY)
shortcut = QShortcut(QKeySequence(Qt.Key_Escape), widget)
shortcut.activated.connect(widget.close)

# start widget
widget.show()
sys.exit(app.exec_())
