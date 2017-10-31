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
                     'English': ['english', 'English', 'Englisch', 'englisch'] }

    language1 = sys.argv[1]
    language2 = sys.argv[2]

    # reduce to english terms
    for key, value in language_dict.items():
        if language1 in value:
            language1 = key

    for key, value in language_dict.items():
        if language2 in value:
            language2 = key

    # reduce possibilities of word pairs to three variants
    if language2 == 'French':
        language1, language2 = language2, language1

    if language1 == 'German':
        language1, language2 = language2, language1

    languagePair = '{language1}_{language2}'.format(language1=language1, language2=language2)
    return language1, language2, languagePair

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

        # set items for table
        self.item1 = self.mainTable.horizontalHeaderItem(0)
        self.item2 = self.mainTable.horizontalHeaderItem(1)

        self.item1.setText('{}'.format(self.language1))
        self.item2.setText('{}'.format(self.language2))

        self.language1Label.setText('    {}'.format(self.language1))
        self.language2Label.setText(' {}'.format(self.language2))

        self.solutionLabel.setText(' ')

        # create table in database
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('''CREATE TABLE IF NOT EXISTS Main(
                id INTEGER PRIMARY KEY,
                language_one TEXT,
                language_two TEXT,
                tableLevel INTEGER)''')

        # save changes to database
        self.dbConn.commit()

        # save settings to file
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope,
            'PyVocTrainer', 'PyVocTrainer')

        # add signals and slots
        self.addVocButton.clicked.connect(self.add_button_clicked)
        self.voc2LineEdit.returnPressed.connect(self.add_button_clicked)
        self.removeRowButton.clicked.connect(self.remove_row_clicked)
        self.actionImport.triggered.connect(self.import_data)
        self.startLearningButton.clicked.connect(self.get_next_word)
        self.howeverTrueButton.clicked.connect(lambda:
         self.set_answer_true(self.dictionary[self.lineEdit_1.text()],
         self.lineEdit_1.text()))

        self.lineEdit_2.returnPressed.connect(lambda:
         self.check_entry(self.dictionary[self.lineEdit_1.text()],
         self.lineEdit_2.text(), self.lineEdit_1.text()))

        geometry = self.vocabsLearnedLabel.geometry()
        # geometry = self.vocabsLearnedLabel.setGeometry(QRect(60, 0, 100, 50))
        self.vocabsLearnedLabel.setText("Words learned in current session:")

        # initialize dictionary
        self.dictionary = {}
        self.load_initial_settings()
        self.dictKeys = list(self.dictionary.keys())

    def load_initial_settings(self):
        '''Loads the initial settings for the application. Sets the mainTable
        columns width. '''

        # select all items from Main
        self.dbCursor.execute('''SELECT * FROM Main''')

        # returns a python list
        allRows = self.dbCursor.fetchall()

        for row_inx, row in enumerate(allRows):
            self.insert_item(self.mainTable, row_inx, row)
            self.dictionary[row[1]] = [row[2], int(row[3])]

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
        dummy = self.mainTable.rowCount() + 1   # for correct indexing in insert_item method

        self.add_to_table([dummy, voc1, voc2, initLevel])

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
        self.dbCursor.execute('''INSERT INTO Main VALUES (?, ?, ?, ?)''',
         parameters)
        self.dbConn.commit()

    def update_level(self, language1, language2, level):
        '''Updates the level in table after correct answer.'''

        # commit changes to Database
        parameters = (level, language1)
        self.dbCursor.execute(
        '''UPDATE Main SET level = ? WHERE language_one = ?''', parameters)

        self.dbConn.commit()


        # update table in application
        # make a tuple because sqlite needs a tuple as input
        language1_tuple = (language1, )
        self.dbCursor.execute('''SELECT * FROM Main WHERE language_one = ?''', language1_tuple)

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
            self.dbCursor.execute('''DELETE FROM Main WHERE Language_One = ?''',
             currentVoc)
            self.dbConn.commit()
            self.mainTable.removeRow(currentRow)

    def get_next_word(self):
        '''Chooses a word from the dictionary (keys) and writes it into the first
        line edit.'''

        # choose a random number to select a certain key from the dictionary
        e = numpy.random.randint(len(self.dictionary))

        # fill the first text-edit-box with a word from the dictionary
        self.lineEdit_1.setText(self.dictKeys[e])
        self.lineEdit_2.clear()

        # show the level value
        values = self.dictionary[self.dictKeys[e]]
        level_text = str(values[1])
        self.levelText.setText(level_text)

        # set focus on second line edit
        self.lineEdit_2.setFocus()

        return self.dictKeys[e]

    def correct_answer_given(self, word2, word3):
        '''Handles all the stuff which needs to be done if the answer was
        correct'''
        self.get_next_word()

        # update line edits and labels
        self.lineEdit_2.clear()
        self.lineEdit_2.setFocus()

        count = int(self.vocabsLearned.text())
        count += 1
        self.vocabsLearned.setText(str(count))

        # update level
        values = self.dictionary[word3]
        level = values[1]
        new_level = level + 1
        self.dictionary[word3] = [word2, new_level]
        self.update_level(word3, word2, new_level)

    def check_entry(self, word1, word2, word3):
        '''Returns True if the word1 and word2 are a key-value-pair and False
        if not.'''
        # extract correct word from the list in dictionary according to
        # first line edit -- second language -- correct word
        word1 = str(word1[0])
        word1 = word1.strip('\t')
        # the word in second line edit -- second language -- tested word
        word2 = str(word2)
        # the respective word in - first language
        word3 = str(word3)

        print(word1, word2)

        if word1 == word2:
            # correct answer
            print (True)
            self.assertionLabel.setText("Correct!")
            self.correct_answer_given(word2, word3)
            return True
        else:
            # incorrect answer
            print (False)
            self.assertionLabel.setText("Unfortunately wrong!")
            self.solutionLabel.setText(word1)
            self.lineEdit_2.setFocus()
            self.lineEdit_2.selectAll()
            self.continueButton.clicked.connect(self.get_next_word)
            self.continueButton.pressed.connect(self.get_next_word)
            return False

    def import_data(self):
        '''
        Imports whole vocabulary from txt file into dictionary.

        Column 1: First Language
        Column 2: Second Language
        Column 3: Level (1-5)
        '''

        inputfile = QFileDialog.getOpenFileName(parent = None, caption =
        "Import database to a Application", directory = ".", filter =
        "PyVocTrainer CSV (*.txt)")

        print (inputfile[0])
        if inputfile[0]:
            try:
                with open (inputfile[0], "r", newline = '') as infile:
                    reader = csv.reader(infile, delimiter = '\t')
                    for line in reader:
                        print (line)
                        if len(line) == 3:
                            word1 = line[0]
                            translation = line[1]
                            level = int(line[2])
                            self.dictionary[word1] = [translation, level]
                            self.dictKeys.append(word1)
                        elif len(line) == 2:
                            word1 = line[0]
                            translation = line[1]
                            self.dictionary[word1] = [translation, 1]
                            self.dictKeys.append(word1)

            except Exception as msg:
                print ("File not imported.\n The error is\n{}".format(msg))

        else:
            pass

        for entry in self.dictionary:
            liste = self.dictionary[entry]
            translation = liste[0]
            level = liste[1]
            self.add_to_table([entry, translation, level])
            print ('{}\t{}\t{}'.format(entry, translation, level))

    def export_action_triggered(self):
        '''Database export handler.'''
        pass

    def set_answer_true(self, word2, word3):
        '''Carries out basically the same procedure as if the answer were given
        correctly at the beginning

        word2 and word3 according to function check_entry'''

        word2 = str(word2)
        word3 = str(word3)

        self.assertionLabel.setText(" ")
        self.correct_answer_given(word2, word3)
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


    # TODO: Save levels correctly (should work fine)
    # TODO: Level is not updated immediately but only after restart
    # TODO: Use sql dictionary instead of manual dictionary
    # TODO: Include Tooltipps
    # TODO: Split tabs into different windows
    # TODO: Make Widget stretchable
    # TODO: mehr Wörter der unteren Level zur Abfrage auswählen
    # TODO: introduce counting with bars
    # TODO: choose to learn english or french --- DONE
