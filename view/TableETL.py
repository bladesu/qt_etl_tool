# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/TableETL.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 60, 651, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(80, 20, 61, 22))
        self.toolButton.setObjectName("toolButton")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(80, 310, 651, 241))
        self.tableWidget_2.setObjectName("tableWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuTransformer = QtWidgets.QMenu(self.menubar)
        self.menuTransformer.setObjectName("menuTransformer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionETL_designer = QtWidgets.QAction(MainWindow)
        self.actionETL_designer.setObjectName("actionETL_designer")
        self.menuTransformer.addAction(self.actionETL_designer)
        self.menubar.addAction(self.menuTransformer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.menuTransformer.setTitle(_translate("MainWindow", "Transformer"))
        self.actionETL_designer.setText(_translate("MainWindow", "ETL designer"))

