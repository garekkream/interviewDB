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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupDB)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 601, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalQuestion = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalQuestion.setObjectName("verticalQuestion")
        self.gridInfo = QtWidgets.QGridLayout()
        self.gridInfo.setObjectName("gridInfo")
        self.labelID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelID.setMaximumSize(QtCore.QSize(20, 16777215))
        self.labelID.setObjectName("labelID")
        self.gridInfo.addWidget(self.labelID, 0, 0, 1, 1)
        self.spinID = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinID.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinID.setObjectName("spinID")
        self.gridInfo.addWidget(self.spinID, 0, 1, 1, 1)
        self.labelCategory = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCategory.setMinimumSize(QtCore.QSize(60, 0))
        self.labelCategory.setObjectName("labelCategory")
        self.gridInfo.addWidget(self.labelCategory, 0, 2, 1, 1)
        self.lineCategory = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineCategory.setObjectName("lineCategory")
        self.gridInfo.addWidget(self.lineCategory, 0, 3, 1, 1)
        self.verticalQuestion.addLayout(self.gridInfo)
        self.horizontalDescription = QtWidgets.QHBoxLayout()
        self.horizontalDescription.setObjectName("horizontalDescription")
        self.labelDescription = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelDescription.setObjectName("labelDescription")
        self.horizontalDescription.addWidget(self.labelDescription)
        self.plainDescription = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainDescription.setMinimumSize(QtCore.QSize(0, 0))
        self.plainDescription.setMaximumSize(QtCore.QSize(16777215, 100))
        self.plainDescription.setObjectName("plainDescription")
        self.horizontalDescription.addWidget(self.plainDescription)
        self.verticalQuestion.addLayout(self.horizontalDescription)
        self.horizontalType = QtWidgets.QHBoxLayout()
        self.horizontalType.setObjectName("horizontalType")
        self.radioTest = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioTest.setObjectName("radioTest")
        self.horizontalType.addWidget(self.radioTest)
        self.radioOpen = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioOpen.setObjectName("radioOpen")
        self.horizontalType.addWidget(self.radioOpen)
        self.radioCode = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioCode.setObjectName("radioCode")
        self.horizontalType.addWidget(self.radioCode)
        self.verticalQuestion.addLayout(self.horizontalType)
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

        MainWindow.setFixedSize(797, 493)

        self.setupSignals()
        self.setupWidgets()

        self.currentItem = ""

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
        self.labelID.setText(_translate("MainWindow", "ID:"))
        self.labelCategory.setText(_translate("MainWindow", "Category:"))
        self.labelDescription.setText(_translate("MainWindow", "Description:"))
        self.radioTest.setText(_translate("MainWindow", "Test (6 options max)"))
        self.radioOpen.setText(_translate("MainWindow", "Open"))
        self.radioCode.setText(_translate("MainWindow", "Code"))
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

        self.pushAdd.clicked.connect(self.addQuestion)
        self.pushDel.clicked.connect(self.removeQuestion)

        self.listQuestions.clicked.connect(self.changeQuestion)

        self.spinID.valueChanged.connect(self.changeID)

        self.lineCategory.editingFinished.connect(self.changeCategory)
        self.plainDescription.textChanged.connect(self.changeDescription)

    def setupWidgets(self):
        self.__disableWidgets()

    def __disableWidgets(self):
        self.pushAdd.setEnabled(False)
        self.pushDel.setEnabled(False)
        self.lineCategory.setEnabled(False)
        self.lineDbAuthor.setEnabled(False)
        self.lineDbName.setEnabled(False)
        self.spinID.setEnabled(False)
        self.radioCode.setEnabled(False)
        self.radioOpen.setEnabled(False)
        self.radioTest.setEnabled(False)
        self.plainDescription.setEnabled(False)

    def __enableWidgets(self):
        self.pushAdd.setEnabled(True)
        self.pushDel.setEnabled(True)
        self.lineCategory.setEnabled(True)
        self.lineDbAuthor.setEnabled(True)
        self.lineDbName.setEnabled(True)
        self.spinID.setEnabled(True)
        self.radioCode.setEnabled(True)
        self.radioOpen.setEnabled(True)
        self.radioTest.setEnabled(True)
        self.plainDescription.setEnabled(True)

    def __get_metadata(self):
        self.lineDbAuthor.setText(self.db.db_get_author())
        self.lineDbDate.setText(self.db.db_get_timestamp())
        self.lineDbName.setText(self.db.db_get_name())

    def selectNewDb(self):
        log = logging.getLogger(self.selectNewDb.__name__)

        filename = QtWidgets.QFileDialog().getSaveFileName(None, "Create DB...", ".")
        log.debug("Selected file name " + filename[0])

        self.db.db_create(os.path.basename(filename[0]), filename[0])

        self.__get_metadata()
        self.__enableWidgets()

    def selectLoadDatabase(self):
        log = logging.getLogger(self.selectLoadDatabase.__name__)

        model = self.listQuestions.model()
        filename = QtWidgets.QFileDialog().getOpenFileName(None, "Open file...", '.')
        log.debug("Selected file name: " + filename[0])

        self.db.db_set_file_name(filename[0])
        self.db.db_read()

        self.__get_metadata()
        self.__enableWidgets()

        self.listQuestions.addItems(self.db.db_get_questionsList())
        self.listQuestions.setCurrentIndex(model.index(0,0))
        self.currentItem = self.listQuestions.currentItem().text()
        self.fillQuestionFields(self.currentItem)

    def selectSaveDatabase(self):
        log = logging.getLogger(self.selectSaveDatabase.__name__)

        filename = QtWidgets.QFileDialog().getSaveFileName(None, "Create DB...", ".")
        log.debug("Selected file name " + filename[0])

        self.db.db_dump_to_file()

    def selectExit(self):
        log = logging.getLogger(self.selectExit.__name__)

        QtCore.QCoreApplication.instance().quit()

        log.debug("Exiting...")

    def addQuestion(self):
        log = logging.getLogger(self.addQuestion.__name__)

        id = self.db.db_find_free_id()

        if(id is not False):
            questionName = "Question" + str(id) + "@" + self.db.db_get_name()

            log.debug("Adding question: " + questionName)
            self.db.db_add_question(id)
            self.listQuestions.addItem(questionName)

    def removeQuestion(self):
        log = logging.getLogger(self.removeQuestion.__name__)

        node_name = self.listQuestions.currentItem().text()

        log.debug("Trying to remove " + node_name)

        self.db.db_del_question(node_name)
        self.listQuestions.takeItem(self.listQuestions.currentRow())

    def fillQuestionFields(self, node_name):
        question = self.db.db_get_question(node_name)

        self.spinID.setValue(question['id'])
        self.plainDescription.setPlainText(question['descr'])
        self.lineCategory.setText(question['category'])

        return question

    def changeQuestion(self):
        log = logging.getLogger(self.changeQuestion.__name__)

        node_name = self.listQuestions.currentItem().text()
        log.debug(node_name)
        if self.currentItem != node_name:
            self.currentItem = self.listQuestions.currentItem().text()
            question = self.fillQuestionFields(node_name)
            log.debug(question)

    def changeID(self):
        question = self.db.db_get_question(self.currentItem)
        question['id'] = self.spinID.value()

    def changeCategory(self):
        question = self.db.db_get_question(self.currentItem)
        question['category'] = self.lineCategory.text()

    def changeDescription(self):
        log = logging.getLogger("asdasd")
        question = self.db.db_get_question(self.currentItem)
        question['descr'] = self.plainDescription.toPlainText()
        log.debug("asdasdass")
