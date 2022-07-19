# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/SheetTableView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    
    _DISPLAY_BUTTON_OPEN_FILE_1 = '打開領料記錄表'
    _DISPLAY_BUTTON_OPEN_FILE_2 = '打開庫存報表'
    _DISPLAY_TAB_1 = '領料記錄表'
    _DISPLAY_TAB_2 = '庫存報表'
    _DISPLAY_BUTTON_DO_MAPPING = '產生實際庫存報表'
    _DISPLAY_BUTTON_SAVE_FILE = '儲存實際庫存報表' 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 19, 1041, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_loadingFiles = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_loadingFiles.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_loadingFiles.setObjectName("verticalLayout_loadingFiles")
        self.groupBox_1 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_1.setObjectName("groupBox_1")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_1)
        self.tabWidget.setGeometry(QtCore.QRect(-11, 19, 1051, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.sheetNames_1 = QtWidgets.QListWidget(self.tab_1)
        self.sheetNames_1.setGeometry(QtCore.QRect(10, 30, 151, 301))
        self.sheetNames_1.setObjectName("sheetNames_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_1.setGeometry(QtCore.QRect(160, 30, 881, 301))
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_1.setRowCount(0)
        self.openFileButton_1 = QtWidgets.QPushButton(self.tab_1)
        self.openFileButton_1.setGeometry(QtCore.QRect(10, 0, 151, 32))
        self.openFileButton_1.setObjectName("openFileButton_1")
        self.showOpenFile_1 = QtWidgets.QTextEdit(self.tab_1)
        self.showOpenFile_1.setGeometry(QtCore.QRect(160, 0, 881, 31))
        self.showOpenFile_1.setObjectName("showOpenFile_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(160, 30, 881, 301))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.sheetNames_2 = QtWidgets.QListWidget(self.tab_2)
        self.sheetNames_2.setGeometry(QtCore.QRect(10, 30, 151, 301))
        self.sheetNames_2.setObjectName("sheetNames_2")
        self.showOpenFile_2 = QtWidgets.QTextEdit(self.tab_2)
        self.showOpenFile_2.setGeometry(QtCore.QRect(160, 0, 881, 31))
        self.showOpenFile_2.setObjectName("showOpenFile_2")
        self.openFileButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.openFileButton_2.setGeometry(QtCore.QRect(10, 0, 151, 32))
        self.openFileButton_2.setObjectName("openFileButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_loadingFiles.addWidget(self.groupBox_1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 410, 1041, 371))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_exportFile = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_exportFile.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_exportFile.setObjectName("verticalLayout_exportFile")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.mappingButton = QtWidgets.QPushButton(self.groupBox_2)
        self.mappingButton.setGeometry(QtCore.QRect(0, 20, 131, 32))
        self.mappingButton.setObjectName("mappingButton")
        self.exportedTableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.exportedTableWidget.setGeometry(QtCore.QRect(5, 51, 1031, 311))
        self.exportedTableWidget.setObjectName("exportedTableWidget")
        self.exportedTableWidget.setColumnCount(0)
        self.exportedTableWidget.setRowCount(0)
        self.verticalLayout_exportFile.addWidget(self.groupBox_2)
        self.saveFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveFileButton.setGeometry(QtCore.QRect(20, 780, 141, 32))
        self.saveFileButton.setObjectName("saveFileButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open_1 = QtWidgets.QAction(MainWindow)
        self.action_open_1.setObjectName("action_open_1")
        self.action_open_2 = QtWidgets.QAction(MainWindow)
        self.action_open_2.setObjectName("action_open_2")
        self.actionmapping = QtWidgets.QAction(MainWindow)
        self.actionmapping.setObjectName("actionmapping")
        self.actionexport = QtWidgets.QAction(MainWindow)
        self.actionexport.setObjectName("actionexport")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_1.setTitle(_translate("MainWindow", "Loaded files"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>file2</p></body></html>"))
        self.openFileButton_1.setText(_translate("MainWindow", self._DISPLAY_BUTTON_OPEN_FILE_1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", self._DISPLAY_TAB_1))
        self.openFileButton_2.setText(_translate("MainWindow", self._DISPLAY_BUTTON_OPEN_FILE_2))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", self._DISPLAY_TAB_2))
        self.groupBox_2.setTitle(_translate("MainWindow", "Mapped table"))
        self.mappingButton.setText(_translate("MainWindow", self._DISPLAY_BUTTON_DO_MAPPING))
        self.saveFileButton.setText(_translate("MainWindow", self._DISPLAY_BUTTON_SAVE_FILE))
        self.action_open_1.setText(_translate("MainWindow", "$open"))
        self.action_open_2.setText(_translate("MainWindow", "$open"))
        self.actionmapping.setText(_translate("MainWindow", "$mapping"))
        self.actionmapping.setToolTip(_translate("MainWindow", "mapping"))
        self.actionexport.setText(_translate("MainWindow", "$export"))

