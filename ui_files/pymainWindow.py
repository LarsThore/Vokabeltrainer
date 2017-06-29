# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vokabeln_GUI_ver01.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 455)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 661, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.layoutWidget = QtWidgets.QWidget(self.tab1)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 1, 641, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout.addWidget(self.lineEdit_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.language1 = QtWidgets.QLabel(self.layoutWidget)
        self.language1.setMinimumSize(QtCore.QSize(320, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.language1.setFont(font)
        self.language1.setObjectName("language1")
        self.gridLayout.addWidget(self.language1, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startLearningButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startLearningButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.startLearningButton.setAutoDefault(True)
        self.startLearningButton.setDefault(True)
        self.startLearningButton.setObjectName("startLearningButton")
        self.verticalLayout_2.addWidget(self.startLearningButton)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.levelLabel = QtWidgets.QLabel(self.layoutWidget)
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
        self.horizontalLayout_4.addWidget(self.levelLabel)
        self.level = QtWidgets.QLabel(self.layoutWidget)
        self.level.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.level.setFont(font)
        self.level.setAlignment(QtCore.Qt.AlignCenter)
        self.level.setObjectName("level")
        self.horizontalLayout_4.addWidget(self.level)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.language2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.language2.setFont(font)
        self.language2.setObjectName("language2")
        self.gridLayout.addWidget(self.language2, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vocabsLearnedLabel = QtWidgets.QLabel(self.layoutWidget)
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
        self.horizontalLayout_3.addWidget(self.vocabsLearnedLabel)
        self.vocabsLearned = QtWidgets.QLabel(self.layoutWidget)
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
        self.horizontalLayout_3.addWidget(self.vocabsLearned)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.howeverTrueButton = QtWidgets.QPushButton(self.tab1)
        self.howeverTrueButton.setGeometry(QtCore.QRect(50, 290, 151, 51))
        self.howeverTrueButton.setAutoDefault(True)
        self.howeverTrueButton.setDefault(True)
        self.howeverTrueButton.setObjectName("howeverTrueButton")
        self.solutionLabel = QtWidgets.QLabel(self.tab1)
        self.solutionLabel.setGeometry(QtCore.QRect(220, 290, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.solutionLabel.setFont(font)
        self.solutionLabel.setObjectName("solutionLabel")
        self.assertionLabel = QtWidgets.QLabel(self.tab1)
        self.assertionLabel.setGeometry(QtCore.QRect(336, 230, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.assertionLabel.setFont(font)
        self.assertionLabel.setObjectName("assertionLabel")
        self.continueButton = QtWidgets.QPushButton(self.tab1)
        self.continueButton.setGeometry(QtCore.QRect(50, 230, 151, 31))
        self.continueButton.setAutoDefault(True)
        self.continueButton.setDefault(True)
        self.continueButton.setObjectName("continueButton")
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.mainTable = QtWidgets.QTableWidget(self.tab_2)
        self.mainTable.setGeometry(QtCore.QRect(20, 60, 631, 241))
        self.mainTable.setObjectName("mainTable")
        self.mainTable.setColumnCount(3)
        self.mainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(2, item)
        self.mainTable.horizontalHeader().setDefaultSectionSize(160)
        self.mainTable.horizontalHeader().setStretchLastSection(True)
        self.mainTable.verticalHeader().setStretchLastSection(False)
        self.voc1LineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.voc1LineEdit.setGeometry(QtCore.QRect(20, 20, 113, 28))
        self.voc1LineEdit.setObjectName("voc1LineEdit")
        self.voc2LineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.voc2LineEdit.setGeometry(QtCore.QRect(160, 20, 113, 28))
        self.voc2LineEdit.setObjectName("voc2LineEdit")
        self.addVocButton = QtWidgets.QPushButton(self.tab_2)
        self.addVocButton.setGeometry(QtCore.QRect(300, 20, 84, 28))
        self.addVocButton.setObjectName("addVocButton")
        self.removeRowButton = QtWidgets.QPushButton(self.tab_2)
        self.removeRowButton.setGeometry(QtCore.QRect(560, 310, 84, 28))
        self.removeRowButton.setObjectName("removeRowButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 686, 25))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.continueButton)
        MainWindow.setTabOrder(self.continueButton, self.howeverTrueButton)
        MainWindow.setTabOrder(self.howeverTrueButton, self.startLearningButton)
        MainWindow.setTabOrder(self.startLearningButton, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.voc2LineEdit)
        MainWindow.setTabOrder(self.voc2LineEdit, self.addVocButton)
        MainWindow.setTabOrder(self.addVocButton, self.removeRowButton)
        MainWindow.setTabOrder(self.removeRowButton, self.mainTable)
        MainWindow.setTabOrder(self.mainTable, self.voc1LineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.language1.setText(_translate("MainWindow", "Language1"))
        self.startLearningButton.setText(_translate("MainWindow", "Start Learning"))
        self.levelLabel.setText(_translate("MainWindow", " Level"))
        self.level.setText(_translate("MainWindow", "1"))
        self.language2.setText(_translate("MainWindow", "Language2"))
        self.vocabsLearnedLabel.setText(_translate("MainWindow", "Words learned in current session:"))
        self.vocabsLearned.setText(_translate("MainWindow", "0"))
        self.howeverTrueButton.setText(_translate("MainWindow", "I had the \n"
"right answer"))
        self.solutionLabel.setText(_translate("MainWindow", "Solution"))
        self.assertionLabel.setText(_translate("MainWindow", "Right / Wrong"))
        self.continueButton.setText(_translate("MainWindow", "Continue"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vocabulary"))
        self.menuFile.setTitle(_translate("MainWindow", "F&ile"))
        self.menuHelp.setTitle(_translate("MainWindow", "He&lp"))
        self.menuEdit.setTitle(_translate("MainWindow", "E&dit"))
        self.actionImport.setText(_translate("MainWindow", "&Import"))
        self.actionExport.setText(_translate("MainWindow", "&Export"))
        self.actionExit.setText(_translate("MainWindow", "E&xit"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionPreferences.setText(_translate("MainWindow", "&Preferences"))

