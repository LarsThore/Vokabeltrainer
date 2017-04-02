#! -*- coding:utf8 -*- #
__appname__ = 'PyVocabularyApp'
__module__ = 'main'

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import re
import sys
import os
import logging

from ui_files import pymainWindow
import sqlite3

# set the default path of the application to HOME/AppDataManager directory
# (soft-coding)
appDataPath = os.environ['HOME'] + '/VocTrainer/'

# if the path does not exist create it
if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception:
        appDataPath = os.getcwd()

# Logging; format
logging.basicConfig(filename= appDataPath + 'pydatamanager.log',
    format = '%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s\
     - %(funcname)-15s - %(lineno)-6d - %(message)s')

# define the module name in the basic Configuration
logger = logging.getLogger(name = 'main-gui')



class Main(QMainWindow, pymainWindow.Ui_MainWindow):
    '''Class inherits from Qt.QMainWindow class and from class built by the
    QtDesigner'''

    # make Database path for table containing the vocabulary
    dbPath = appDataPath + 'pydata.db'
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # create table in database
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('''CREATE TABLE IF NOT EXISTS Main(id INTEGER\
            PRIMARY KEY, language_one TEXT, language_two TEXT, level TEXT)''')

        # save changes to database
        self.dbConn.commit()

        # save settings to file
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope,
            'PyDataManager', 'PyDataManager')

        self.addVocButton.clicked.connect(self.add_button_clicked)
        self.removeRowButton.clicked.connect(self.remove_row_clicked)

        self.load_initial_settings()

    def load_initial_settings(self):
        '''Loads the initial settings for the application. Sets the mainTable
        columns width. '''
        # select all items from Main
        self.dbCursor.execute('''SELECT * FROM Main''')
        allRows = self.dbCursor.fetchall()

        for row in allRows:
            inx = allRows.index(row)
            self.mainTable.insertRow(inx)
            # insert a QTableWidgetItem in the table
            self.mainTable.setItem(inx, 0, QTableWidgetItem(row[1]))
            self.mainTable.setItem(inx, 1, QTableWidgetItem(row[2]))
            self.mainTable.setItem(inx, 2, QTableWidgetItem(str(row[3])))

    def add_button_clicked(self):
        '''Calls the validate_fields method and adds the items to the table
        if true. '''
        voc1 = self.voc1LineEdit.text()
        voc2 = self.voc2LineEdit.text()

        initLevel = str(1)

        # check if field entry has correct structure
        # if not self.validate_fields():
        #     return False

        currentRowCount = self.mainTable.rowCount()

        self.mainTable.insertRow(currentRowCount)
        self.mainTable.setItem(currentRowCount, 0, QTableWidgetItem(voc1))
        self.mainTable.setItem(currentRowCount, 1, QTableWidgetItem(voc2))
        self.mainTable.setItem(currentRowCount, 2, QTableWidgetItem(initLevel))

        # commit changes to Database
        parameters = (None, voc1, voc2, str(initLevel))
        self.dbCursor.execute('''INSERT INTO Main VALUES (?, ?, ?, ?)''',
         parameters)
        self.dbConn.commit()

        self.voc1LineEdit.clear()
        self.voc2LineEdit.clear()
        self.voc1LineEdit.setFocus()

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

    def validate_fields(self):
        '''Validates the QLineEdits based on RegEx '''
        # select one column from the table
        self.dbCursor.execute('''SELECT username FROM Main''')
        usernames = self.dbCursor.fetchall()
        for username_ in usernames:
            if self.userName.text() in username_[0]:
                QMessageBox.warning(self,'Warning!','Such username already exists!')
                return False

        # regaular expression match
        # ^[2-9] --> begins with a 2, 3, 4, ... or 9
        # one digit, two digits - three digits - four digits
        # e.g. 673-734-7384
        if not re.match('^[2-9]\d{2}-\d{3}-\d{4}', self.phoneNumber.text()):
            QMessageBox.warning(self, 'Warning!', 'Phone number seems incorrect!')
            return False

        return True

    def import_action_triggered(self):
        '''Database import handler.'''
        pass

    def export_action_triggered(self):
        '''Database export handler.'''
        pass

    def preferences_action_triggered(self):
        '''Fires up the Preferences dialog. '''
        pass

    def about_action_triggered(self):
        '''Opens the about dialog. '''
        pass

    def exit_action_triggered(self):
        '''Closes the application. '''
        pass



def main():
    QCoreApplication.setApplicationName('PyDataManager')
    QCoreApplication.setApplicationVersion('0.1')
    QCoreApplication.setOrganizationName('PyDataManager')
    QCoreApplication.setOrganizationDomain('pydatamanager.com')

    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
