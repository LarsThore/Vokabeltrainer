#! -*- coding:utf8 -*- #
__appname__ = 'PyVocabularyApp'
__module__ = 'main'

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import re           # system commands
import sys          # system commands
import os           # system commands
import subprocess   # system commands
import logging
import csv          # import/export
import numpy        # scientific computing
import sqlite3      # tables

from pair import Pair
from memory import Memory

from numpy.random import choice

# ------------- rcc and uic automation ----------------
# (from Peter Bouda: PyQt und PySide)

bindir = '/usr/bin'

uic_path = os.path.join(bindir, 'pyuic5')
ui_path = 'ui_files'
out_path_ui = 'ui_files'
ui_files = { 'mainWindow.ui' : 'pymainWindow.py'}

for file in ui_files:
    file_path = os.path.join(ui_path, file)
    out_file_path = os.path.join(out_path_ui, ui_files[file])
    subprocess.call([uic_path, file_path, '-o', out_file_path])

from ui_files import pymainWindow

#               ----------------------------

def voc_logging(languagePair):

    # set the default path of the application to HOME/AppDataManager directory
    appDataPath = os.environ['HOME'] + '/VocTrainer/' + str(languagePair)

    # if the path does not exist create it
    if not os.path.exists(appDataPath):
        try:
            os.makedirs(appDataPath)
        except Exception:
            appDataPath = os.getcwd()

    # Logging; format
    logging.basicConfig(filename= appDataPath + 'pyvoctrainer.log',
        format = '%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s\
         - %(funcName)-15s - %(lineno)-6d - %(message)s')

    # define the module name in the basic Configuration
    logger = logging.getLogger(name = 'main-gui')

    return appDataPath

def get_languagePair():

    language_dict = {'French': ['french', 'French', 'Französisch', 'französisch',
                                                        'Francais', 'francais'],
                     'German': ['deutsch', 'Deutsch', 'German', 'german'],
                     'English': ['english', 'English', 'Englisch', 'englisch'],
                     'Persian': ['persian', 'Persian', 'Persisch', 'persich',
                                 'Iranian', 'iranian', 'Iranisch', 'iranisch'],
                     'Mathematic': ['mathematic', 'Mathematic', 'mathematische',
                                     'Mathematische'],
                     'Definitions': ['definitions', 'Definition', 'Definitionen']}

    try:
        l1 = sys.argv[1]
        l2 = sys.argv[2]
    except IndexError:
        l1 = input('Please type in the language you know (your mother tongue): ')
        l2 = input('Now, please type in the language you want to learn: ')

    # reduce to english terms
    for key, value in language_dict.items():
        if l1 in value:
            l1 = key

    for key, value in language_dict.items():
        if l2 in value:
            l2 = key

    # standardize program names
    # l1_l2 = sorted([l1, l2])
    #
    # l1 = l1_l2[0]
    # l2 = l1_l2[1]

    # reduce possibilities of word pairs to three variants
    if l2 == 'French':
        l1, l2 = l2, l1

    if l1 == 'German':
        l1, l2 = l2, l1

    languagePair = '{language1}_{language2}'.format(language1=l1, language2=l2)

    return l1, l2, languagePair

language1, language2, pair = get_languagePair()
path = voc_logging(pair)

class Main(QMainWindow, pymainWindow.Ui_MainWindow):
    '''Class inherits from Qt.QMainWindow class and from class built by the
    QtDesigner'''

    # make Database path for table containing the vocabulary
    dbPath = path + 'pyvoc.db'
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, language1, language2, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.language1 = str(language1)
        self.language2 = str(language2)

        self.switch = 1

        # initialize pair list
        self.pair_list = list()

        self.make_table()
        self.load_settings()
        self.load_table()
        self.set_texts_and_labels()
        self.set_signals_and_slots()
        self.adjust_table_headers()

        self.startMemoryButton.pressed.connect(self.start_memory)

    def start_memory(self):
        self.startMemoryButton.setParent(None)
        self.startMemoryButton.deleteLater()
        self.startMemoryButton = None

        self.gridLayout.addWidget(Memory(QRect(10, 10, 1065, 685), self,
                                            self.pair_list, self.tab3))

    def adjust_table_headers(self):

        header = self.mainTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setDefaultSectionSize(100)

    def make_table(self):

        # create table in database
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('''CREATE TABLE IF NOT EXISTS Main(
        id INTEGER PRIMARY KEY,
        language_one TEXT,
        language_two TEXT,
        tableLevel INTEGER)''')

        # save changes to database
        self.dbConn.commit()

    def set_texts_and_labels(self):

        self.item1 = self.mainTable.horizontalHeaderItem(0)
        self.item2 = self.mainTable.horizontalHeaderItem(1)

        self.item1.setText('{}'.format(self.language1))
        self.item2.setText('{}'.format(self.language2))

        self.language1Label.setText('    {}'.format(self.language1))
        self.language2Label.setText(' {}'.format(self.language2))

        self.solutionLabel.setText(' ')

        self.language1Button.setText('{}'.format(language1))
        self.language2Button.setText('{}'.format(language2))

    def set_signals_and_slots(self):

        self.addVocButton.clicked.connect(self.add_button_clicked)
        self.voc2LineEdit.returnPressed.connect(self.add_button_clicked)
        self.removeRowButton.clicked.connect(self.remove_row_clicked)
        self.actionImport.triggered.connect(self.import_data)
        self.startLearningButton.clicked.connect(self.get_next_word)

        self.continueButton.clicked.connect(self.get_next_word)
        self.continueButton.pressed.connect(self.get_next_word)

        self.language1Button.clicked.connect(lambda: self.change_switch(1))
        self.language2Button.clicked.connect(lambda: self.change_switch(2))
        self.languageBothButton.clicked.connect(lambda: self.change_switch(0))

        self.howeverTrueButton.clicked.connect(lambda:
                self.set_answer_true(self.lineEdit_1.text()))

        self.lineEdit_2.returnPressed.connect(lambda:
                self.check_entry(self.lineEdit_2.text()))

    def load_settings(self):
        '''Loads the initial settings for the application. Sets the mainTable
        columns width. '''

        # save settings to file
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope,
        'PyVocTrainer', 'PyVocTrainer')

        # select all items from Main
        self.dbCursor.execute('''SELECT * FROM Main''')

    def load_table(self):

        # returns a python list
        allRows = self.dbCursor.fetchall()

        for row_inx, row in enumerate(allRows):
            self.insert_item(self.mainTable, row_inx, row)
            pair = Pair(row[1], row[2], self.language1, self.language2, row[3])
            self.pair_list.append(pair)

    def change_switch(self, button):

        if button == 2:
            # default
            self.switch = 1
            self.language1Button.setChecked(False)
            self.languageBothButton.setChecked(False)
            self.language1Label.setText('{}'.format(self.language1))
            self.language2Label.setText('{}'.format(self.language2))
        elif button == 1:
            self.switch = -1
            self.language2Button.setChecked(False)
            self.languageBothButton.setChecked(False)
            self.language1Label.setText('{}'.format(self.language2))
            self.language2Label.setText('{}'.format(self.language1))
        else:
            self.switch = 0
            self.language1Button.setChecked(False)
            self.language2Button.setChecked(False)

    def insert_item(self, table, row_inx, row):

        table.insertRow(row_inx)
        row = list(row)
        print(row)

        for col_inx, value in enumerate(row[1:]):
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, value)
            table.setItem(row_inx, col_inx, item)

    def add_button_clicked(self):
        '''Adds the vocabulary pair to the table.'''

        voc1 = self.voc1LineEdit.text()
        voc2 = self.voc2LineEdit.text()

        initLevel = 1       # integer !

        pair = Pair(voc1, voc2, self.language1, self.language2, 1)

        dummy = self.mainTable.rowCount() + 1   # for correct indexing in insert_item method

        self.add_to_table([dummy, voc1, voc2, initLevel])

        self.pair_list.append(pair)

        self.voc1LineEdit.clear()
        self.voc2LineEdit.clear()
        self.voc1LineEdit.setFocus()

    def add_to_table(self, row):
        '''Adds the vocabulary pair and the level to the table'''

        currentRowCount = self.mainTable.rowCount()
        print(row)
        self.insert_item(self.mainTable, currentRowCount, row)

        # commit changes to Database
        # first parameter automatically defined by sq engine (id number)
        parameters = (None, row[1], row[2], row[3])
        self.dbCursor.execute('''INSERT INTO Main VALUES (?, ?, ?, ?)''', parameters)
        self.dbConn.commit()

    def update_level_in_table(self):
        '''Updates the level in table after correct answer.'''

        # commit changes to Database
        parameters = (self.current_pair.level, self.current_pair.word1)
        self.dbCursor.execute(
        '''UPDATE Main SET tableLevel = ? WHERE language_one = ?''', parameters)

        self.dbConn.commit()

        # update table in application
        # make a tuple because sqlite needs a tuple as input
        word1_tuple = (self.current_pair.word1, )
        self.dbCursor.execute('''SELECT * FROM Main WHERE language_one = ?''', word1_tuple)

        row = self.dbCursor.fetchone()
        print (row, type(row))
        # indexing starts at 3
        inx = row[0] + 3

        self.insert_item(self.mainTable, inx, row)

    def remove_row_clicked(self):
        '''Removes the selected row from the mainTable.'''
        # which row has been selected by the user
        currentRow =self.mainTable.currentRow()

        # if any row is selected
        if currentRow > -1:
            # make a tuple because sqlite needs a tuple as input
            currentVoc = (self.mainTable.item(currentRow, 0).text(), )
            self.dbCursor.execute('''DELETE FROM Main WHERE language_one = ?''', currentVoc)
            self.dbConn.commit()
            self.mainTable.removeRow(currentRow)

    def get_next_word(self):
        '''Chooses a word from the pair list and writes it into the first
        line edit.'''

        # choose a random number to select a certain key from the pair list
        self.current_pair = numpy.random.choice(self.pair_list)

        if self.switch == 1:
            text = self.current_pair.word1
        elif self.switch == -1:
            text = self.current_pair.word2
        elif self.switch == 0:
            self.a = choice([-1, 1])
            if self.a == 1:
                text = self.current_pair.word1
                self.language1Label.setText('{}'.format(self.language1))
                self.language2Label.setText('{}'.format(self.language2))
            elif self.a == -1:
                text = self.current_pair.word2
                self.language1Label.setText('{}'.format(self.language2))
                self.language2Label.setText('{}'.format(self.language1))

        # fill the first text-edit-box with a word from the pair list
        self.lineEdit_1.setText(text)
        self.lineEdit_2.clear()

        # show the level value
        level = self.current_pair.level
        self.levelText.setText(str(level))

        # set focus on second line edit
        self.lineEdit_2.setFocus()

        return text

    def correct_answer_given(self):
        '''Handles all the stuff which needs to be done if the answer was
        correct'''

        self.current_pair.level += 1
        self.update_level_in_table()

        # update line edits and labels
        self.lineEdit_2.clear()
        self.lineEdit_2.setFocus()

        count = int(self.vocabsLearned.text())
        count += 1
        self.vocabsLearned.setText(str(count))

        self.get_next_word()

    def check_entry(self, guess):
        '''Returns True if the correct_word and guess belong to the same pair and False
        if not.'''

        # the word in second line edit -- second language -- tested word
        guess = str(guess)

        if self.switch == 1 or (self.switch == 0 and self.a == 1):
            correct_word = self.current_pair.word2
        elif self.switch == -1 or (self.switch == 0 and self.a == -1):
            correct_word = self.current_pair.word1


        if correct_word == guess:
            # correct answer
            print (True)
            self.assertionLabel.setText("Correct!")
            self.correct_answer_given()
            return True
        else:
            # incorrect answer
            print (False)
            self.assertionLabel.setText("Unfortunately wrong...")
            self.solutionLabel.setText(self.current_pair.word2)
            self.lineEdit_2.setFocus()
            self.lineEdit_2.selectAll()
            return False

    def import_data(self):
        '''
        Imports whole vocabulary from txt file into pair list.

        Column 1: First Language
        Column 2: Second Language
        Column 3: Level (1-5)
        '''

        inputfile = QFileDialog.getOpenFileName(parent = None,
            caption = "Import database to a Application", directory = ".",
            filter = "PyVocTrainer CSV (*.txt)")

        print (inputfile[0])
        if inputfile[0]:
            try:
                with open (inputfile[0], "r", newline = '') as infile:
                    reader = csv.reader(infile, delimiter = '\t')
                    for line in reader:
                        print (line)
                        word1 = line[0]
                        translation = line[1]
                        level = int(line[2]) if len(line)==3 else 1
                        pair = Pair(word1, translation, self.language1, self.language2, level)

            except Exception as msg:
                print ("File not imported.\n The error is\n{}".format(msg))

        else:
            pass

        for pair in self.pair_list:
            self.add_to_table([pair.word1, pair.word2, pair.level])
            print ('{}\t{}\t{}'.format(pair.word1, pair.word2, pair.level))

    def export_action_triggered(self):
        '''Database export handler.'''
        pass

    def set_answer_true(self, word1):
        '''Carries out basically the same procedure as if the answer were given
        correctly at the beginning
        '''

        word1 = str(word1)

        # pair = [e.word2 == True for e in pair_list]
        ### Filter one liner ### filter(lambda x: condition(x), some_list)
        pair = list(filter(lambda x: x.word1 == word1, self.pair_list))
        pair = pair[0]

        print(pair)

        self.assertionLabel.setText(" ")
        self.correct_answer_given()
        return True


def main():
    QCoreApplication.setApplicationName('PyVocTrainer')
    QCoreApplication.setApplicationVersion('0.1')
    QCoreApplication.setOrganizationName('PyVocTrainer')
    QCoreApplication.setOrganizationDomain('PyVocTrainer.com')

    app = QApplication(sys.argv)
    form = Main(language1, language2)

    # place application in screen center
    screenGeometry = QApplication.desktop().screenGeometry()
    x = (screenGeometry.width()-form.width()) / 2
    y = (screenGeometry.height()-form.height()) / 2
    form.move(x, y)

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()


# TODO: Level is not updated immediately but only after restart
# TODO: mehr Wörter der unteren Level zur Abfrage auswählen
# TODO: wechseln können welche Sprache abgefragt wird
# TODO: (Include Tooltipps)
# TODO: (Split tabs into different windows)
# TODO: introduce counting with bars
# TODO: Make Widget stretchable
