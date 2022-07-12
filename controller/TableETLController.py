# -*- coding: utf-8 -*-
from PyQt5 import QtCore 
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from view.TableETL import Ui_MainWindow

from model.Table import Table
from util.ExcelLoader import ExcelLoader
from util.TableWidgetCreator import TableWidgetCreator

class TableETLController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        excel_file_path = './testdata/excel_file.xlsx'
        worksheet_name = 'sheet1'
        table:Table = ExcelLoader(excel_file_path, worksheet_name).get_table()
        TableWidgetCreator().fill(table, self.ui.tableWidget)
        TableWidgetCreator().fill(table, self.ui.tableWidget_2)

        

        