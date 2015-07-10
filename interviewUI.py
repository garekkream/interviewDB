# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interview.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

import classDatabase
import logging

logging.basicConfig(level=logging.DEBUG)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
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
        self.menuDatabase.addAction(self.actionLoad)
        self.menuDatabase.addAction(self.actionSave)
        self.menuDatabase.addAction(self.actionExit)
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.setupSignals()

        self.db = classDatabase.database()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def setupSignals(self):
        self.actionLoad.triggered.connect(self.selectLoadDatabase)
        self.actionSave.triggered.connect(self.selectSaveDatabase)
        self.actionExit.triggered.connect(self.selectExit)

    def selectLoadDatabase(self):
        log = logging.getLogger(self.selectLoadDatabase.__name__)

        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open file...", '.')
        log.debug("Selected file name: " + filename)

        self.db.db_set_file_name(filename)

    def selectSaveDatabase(self):
        log = logging.getLogger(self.selectSaveDatabase.__name__)

    def selectExit(self):
        log = logging.getLogger(self.selectExit.__name__)

        QtCore.QCoreApplication.instance().quit()

        log.debug("Exiting...")
