# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 782)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1071, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.howeverTrueButton = QtWidgets.QPushButton(self.tab1)
        self.howeverTrueButton.setGeometry(QtCore.QRect(50, 510, 151, 51))
        self.howeverTrueButton.setAutoDefault(True)
        self.howeverTrueButton.setDefault(True)
        self.howeverTrueButton.setObjectName("howeverTrueButton")
        self.solutionLabel = QtWidgets.QLabel(self.tab1)
        self.solutionLabel.setGeometry(QtCore.QRect(300, 510, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.solutionLabel.setFont(font)
        self.solutionLabel.setObjectName("solutionLabel")
        self.assertionLabel = QtWidgets.QLabel(self.tab1)
        self.assertionLabel.setGeometry(QtCore.QRect(310, 423, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.assertionLabel.setFont(font)
        self.assertionLabel.setObjectName("assertionLabel")
        self.continueButton = QtWidgets.QPushButton(self.tab1)
        self.continueButton.setGeometry(QtCore.QRect(50, 420, 151, 31))
        self.continueButton.setAutoDefault(True)
        self.continueButton.setDefault(True)
        self.continueButton.setObjectName("continueButton")
        self.language1Label = QtWidgets.QLabel(self.tab1)
        self.language1Label.setGeometry(QtCore.QRect(51, 219, 320, 25))
        self.language1Label.setMinimumSize(QtCore.QSize(320, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.language1Label.setFont(font)
        self.language1Label.setObjectName("language1Label")
        self.language2Label = QtWidgets.QLabel(self.tab1)
        self.language2Label.setGeometry(QtCore.QRect(534, 219, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.language2Label.setFont(font)
        self.language2Label.setObjectName("language2Label")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_1.setGeometry(QtCore.QRect(52, 295, 421, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 297, 421, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.startLearningButton = QtWidgets.QPushButton(self.tab1)
        self.startLearningButton.setGeometry(QtCore.QRect(536, 43, 241, 28))
        self.startLearningButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.startLearningButton.setAutoDefault(True)
        self.startLearningButton.setDefault(True)
        self.startLearningButton.setObjectName("startLearningButton")
        self.levelLabel = QtWidgets.QLabel(self.tab1)
        self.levelLabel.setGeometry(QtCore.QRect(537, 78, 171, 40))
        self.levelLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.levelLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.levelLabel.setFont(font)
        self.levelLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.levelLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.levelLabel.setObjectName("levelLabel")
        self.levelText = QtWidgets.QLabel(self.tab1)
        self.levelText.setGeometry(QtCore.QRect(770, 80, 16, 35))
        self.levelText.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.levelText.setFont(font)
        self.levelText.setAlignment(QtCore.Qt.AlignCenter)
        self.levelText.setObjectName("levelText")
        self.vocabsLearnedLabel = QtWidgets.QLabel(self.tab1)
        self.vocabsLearnedLabel.setGeometry(QtCore.QRect(60, 40, 201, 81))
        self.vocabsLearnedLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.vocabsLearnedLabel.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vocabsLearnedLabel.setFont(font)
        self.vocabsLearnedLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vocabsLearnedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.vocabsLearnedLabel.setWordWrap(True)
        self.vocabsLearnedLabel.setObjectName("vocabsLearnedLabel")
        self.vocabsLearned = QtWidgets.QLabel(self.tab1)
        self.vocabsLearned.setGeometry(QtCore.QRect(320, 60, 16, 50))
        self.vocabsLearned.setMinimumSize(QtCore.QSize(0, 50))
        self.vocabsLearned.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vocabsLearned.setFont(font)
        self.vocabsLearned.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vocabsLearned.setAlignment(QtCore.Qt.AlignCenter)
        self.vocabsLearned.setWordWrap(True)
        self.vocabsLearned.setObjectName("vocabsLearned")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.mainTable = QtWidgets.QTableWidget(self.tab2)
        self.mainTable.setGeometry(QtCore.QRect(120, 60, 821, 581))
        self.mainTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainTable.setObjectName("mainTable")
        self.mainTable.setColumnCount(3)
        self.mainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.mainTable.setHorizontalHeaderItem(2, item)
        self.mainTable.horizontalHeader().setDefaultSectionSize(350)
        self.mainTable.horizontalHeader().setMinimumSectionSize(80)
        self.mainTable.horizontalHeader().setStretchLastSection(False)
        self.mainTable.verticalHeader().setStretchLastSection(False)
        self.voc1LineEdit = QtWidgets.QLineEdit(self.tab2)
        self.voc1LineEdit.setGeometry(QtCore.QRect(20, 20, 351, 28))
        self.voc1LineEdit.setObjectName("voc1LineEdit")
        self.voc2LineEdit = QtWidgets.QLineEdit(self.tab2)
        self.voc2LineEdit.setGeometry(QtCore.QRect(390, 20, 351, 28))
        self.voc2LineEdit.setObjectName("voc2LineEdit")
        self.addVocButton = QtWidgets.QPushButton(self.tab2)
        self.addVocButton.setGeometry(QtCore.QRect(773, 20, 121, 28))
        self.addVocButton.setObjectName("addVocButton")
        self.removeRowButton = QtWidgets.QPushButton(self.tab2)
        self.removeRowButton.setGeometry(QtCore.QRect(903, 20, 121, 28))
        self.removeRowButton.setObjectName("removeRowButton")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.memoWidget = QtWidgets.QWidget(self.tab3)
        self.memoWidget.setGeometry(QtCore.QRect(0, 0, 1071, 691))
        self.memoWidget.setBaseSize(QtCore.QSize(1050, 660))
        self.memoWidget.setObjectName("memoWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.memoWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1061, 681))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.startMemoryButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startMemoryButton.sizePolicy().hasHeightForWidth())
        self.startMemoryButton.setSizePolicy(sizePolicy)
        self.startMemoryButton.setMaximumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startMemoryButton.setFont(font)
        self.startMemoryButton.setObjectName("startMemoryButton")
        self.gridLayout.addWidget(self.startMemoryButton, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1094, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.voc1LineEdit, self.voc2LineEdit)
        MainWindow.setTabOrder(self.voc2LineEdit, self.addVocButton)
        MainWindow.setTabOrder(self.addVocButton, self.howeverTrueButton)
        MainWindow.setTabOrder(self.howeverTrueButton, self.startLearningButton)
        MainWindow.setTabOrder(self.startLearningButton, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.continueButton)
        MainWindow.setTabOrder(self.continueButton, self.removeRowButton)
        MainWindow.setTabOrder(self.removeRowButton, self.mainTable)
        MainWindow.setTabOrder(self.mainTable, self.lineEdit_1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.howeverTrueButton.setText(_translate("MainWindow", "I had the \n"
"right answer"))
        self.solutionLabel.setText(_translate("MainWindow", "Solution"))
        self.assertionLabel.setText(_translate("MainWindow", "Right / Wrong"))
        self.continueButton.setText(_translate("MainWindow", "Continue"))
        self.language1Label.setText(_translate("MainWindow", "Language1"))
        self.language2Label.setText(_translate("MainWindow", "Language2"))
        self.startLearningButton.setText(_translate("MainWindow", "Start Learning"))
        self.levelLabel.setText(_translate("MainWindow", " Level"))
        self.levelText.setText(_translate("MainWindow", "1"))
        self.vocabsLearnedLabel.setText(_translate("MainWindow", "Words learned in current session:"))
        self.vocabsLearned.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Learning"))
        item = self.mainTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Language_One"))
        item = self.mainTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Language_Two"))
        item = self.mainTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Level"))
        self.voc1LineEdit.setPlaceholderText(_translate("MainWindow", "1st language"))
        self.voc2LineEdit.setPlaceholderText(_translate("MainWindow", "2nd language"))
        self.addVocButton.setToolTip(_translate("MainWindow", "Add vocabulary pair"))
        self.addVocButton.setText(_translate("MainWindow", "Add"))
        self.removeRowButton.setToolTip(_translate("MainWindow", "Remove vocabulary pair"))
        self.removeRowButton.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Vocabulary"))
        self.startMemoryButton.setText(_translate("MainWindow", "Start Memory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Memory"))
        self.menuFile.setTitle(_translate("MainWindow", "F&ile"))
        self.menuHelp.setTitle(_translate("MainWindow", "He&lp"))
        self.menuEdit.setTitle(_translate("MainWindow", "E&dit"))
        self.actionImport.setText(_translate("MainWindow", "&Import"))
        self.actionExport.setText(_translate("MainWindow", "&Export"))
        self.actionExit.setText(_translate("MainWindow", "E&xit"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionPreferences.setText(_translate("MainWindow", "&Preferences"))

