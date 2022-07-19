# -*- coding: utf-8 -*-
from PyQt5 import QtCore 
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from model.AggregateOperation import *
from misc.AggregateFunctionType import *
from misc.AggregateDimension import *
from operation.SelectOperation import *
from view.TableETL import Ui_MainWindow

from model.Table import Table
from util.ExcelLoader import ExcelLoader
from util.TableWidgetCreator import TableWidgetCreator

class TableETLController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # TODO hardcoded file
        excel_file_path = './testdata/庫存.xlsx'
        worksheet_name = 'Sheet1'
        table: Table = ExcelLoader(excel_file_path, worksheet_name).get_table()
        tables: dict = ExcelLoader(excel_file_path).get_tables()

        #operation = SelectOperation(table, 0, 0)
        
        
        
        TableWidgetCreator().fill(tables.values[0], self.ui.tableWidget)
        #TableWidgetCreator().fill(tables.get, self.ui.tableWidget_2)

        

        