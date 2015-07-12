# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interview.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import classDatabase
import logging
import os

logging.basicConfig(level=logging.DEBUG)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 801, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tabEditor = QtWidgets.QWidget()
        self.tabEditor.setObjectName("tabEditor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabEditor)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 786, 411))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalEditorMain = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalEditorMain.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalEditorMain.setObjectName("horizontalEditorMain")
        self.verticalQuestions = QtWidgets.QVBoxLayout()
        self.verticalQuestions.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalQuestions.setObjectName("verticalQuestions")
        self.listQuestions = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listQuestions.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listQuestions.setObjectName("listQuestions")
        self.verticalQuestions.addWidget(self.listQuestions)
        self.horizontalOperations = QtWidgets.QHBoxLayout()
        self.horizontalOperations.setContentsMargins(-1, -1, -1, 0)
        self.horizontalOperations.setSpacing(6)
        self.horizontalOperations.setObjectName("horizontalOperations")
        self.pushAdd = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushAdd.setObjectName("pushAdd")
        self.horizontalOperations.addWidget(self.pushAdd)
        self.pushDel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushDel.setObjectName("pushDel")
        self.horizontalOperations.addWidget(self.pushDel)
        self.verticalQuestions.addLayout(self.horizontalOperations)
        self.horizontalEditorMain.addLayout(self.verticalQuestions)
        self.verticalSettings = QtWidgets.QVBoxLayout()
        self.verticalSettings.setObjectName("verticalSettings")
        self.groupQuestion = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupQuestion.setMinimumSize(QtCore.QSize(600, 100))
        self.groupQuestion.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupQuestion.setObjectName("groupQuestion")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupQuestion)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 29, 581, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelDbName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelDbName.setObjectName("labelDbName")
        self.gridLayout.addWidget(self.labelDbName, 0, 0, 1, 1)
        self.lineDbName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineDbName.setObjectName("lineDbName")
        self.gridLayout.addWidget(self.lineDbName, 0, 2, 1, 1)
        self.labelDbDate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelDbDate.setObjectName("labelDbDate")
        self.gridLayout.addWidget(self.labelDbDate, 0, 3, 1, 1)
        self.lineDbDate = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineDbDate.setReadOnly(True)
        self.lineDbDate.setClearButtonEnabled(False)
        self.lineDbDate.setObjectName("lineDbDate")
        self.gridLayout.addWidget(self.lineDbDate, 0, 4, 1, 1)
        self.labelDbAuthor = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelDbAuthor.setObjectName("labelDbAuthor")
        self.gridLayout.addWidget(self.labelDbAuthor, 1, 0, 1, 1)
        self.lineDbAuthor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineDbAuthor.setObjectName("lineDbAuthor")
        self.gridLayout.addWidget(self.lineDbAuthor, 1, 2, 1, 1)
        self.verticalSettings.addWidget(self.groupQuestion)
        self.groupDB = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupDB.setObjectName("groupDB")
        self.verticalSettings.addWidget(self.groupDB)
        self.horizontalEditorMain.addLayout(self.verticalSettings)
        self.tabWidget.addTab(self.tabEditor, "")
        self.tabGenerator = QtWidgets.QWidget()
        self.tabGenerator.setObjectName("tabGenerator")
        self.tabWidget.addTab(self.tabGenerator, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 22))
        self.menubar.setObjectName("menubar")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNewDb = QtWidgets.QAction(MainWindow)
        self.actionNewDb.setObjectName("actionNewDb")
        self.menuDatabase.addAction(self.actionNewDb)
        self.menuDatabase.addAction(self.actionLoad)
        self.menuDatabase.addAction(self.actionSave)
        self.menuDatabase.addAction(self.actionExit)
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.setupSignals()

        self.db = classDatabase.database()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushAdd.setText(_translate("MainWindow", "+"))
        self.pushDel.setText(_translate("MainWindow", "-"))
        self.groupQuestion.setTitle(_translate("MainWindow", "DB settings:"))
        self.labelDbName.setText(_translate("MainWindow", "DB name:"))
        self.labelDbDate.setText(_translate("MainWindow", "Creation date:"))
        self.labelDbAuthor.setText(_translate("MainWindow", "Author:"))
        self.groupDB.setTitle(_translate("MainWindow", "Question settings:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEditor), _translate("MainWindow", "Editor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGenerator), _translate("MainWindow", "Generator"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNewDb.setText(_translate("MainWindow", "New DB"))

    def setupSignals(self):
        self.actionNewDb.triggered.connect(self.selectNewDb)
        self.actionLoad.triggered.connect(self.selectLoadDatabase)
        self.actionSave.triggered.connect(self.selectSaveDatabase)
        self.actionExit.triggered.connect(self.selectExit)

    def selectNewDb(self):
        log = logging.getLogger(self.selectNewDb.__name__)

    def selectLoadDatabase(self):
        log = logging.getLogger(self.selectLoadDatabase.__name__)

        filename = QtWidgets.QFileDialog().getOpenFileName(None, "Open file...", '.')
        log.debug("Selected file name: " + filename[0])

        self.db.db_set_file_name(filename[0])

    def selectSaveDatabase(self):
        log = logging.getLogger(self.selectSaveDatabase.__name__)

        filename = QtWidgets.QFileDialog().getSaveFileName(None, "Create DB...", ".")
        log.debug("Selected file name " + filename[0])

        self.db.db_create(os.path.basename(filename[0]), filename[0])

    def selectExit(self):
        log = logging.getLogger(self.selectExit.__name__)

        QtCore.QCoreApplication.instance().quit()

        log.debug("Exiting...")
