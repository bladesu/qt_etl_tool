# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem
from view.SheetTableView import Ui_MainWindow
from model.Table import Table
from util.ExcelLoader import ExcelLoader
from util.TableWidgetCreator import TableWidgetCreator
from typing import Dict
from pandas import DataFrame
import pandas as pd
class SheetTableETLController(QMainWindow):
    
    _DISPLAY_OPEN_FILE = '打開檔案'
    _DISPLAY_SAVE_FILE = '儲存檔案'
    _TABLE_1_HEADER = 5
    _TABLE_2_HEADER = 0
    # data
    _COLUMN_ID = '材料編號'
    _COLUMN_AMOUNT_TABLE1 = '數量'
    _COLUMN_AMOUNT_TABLE2 = '庫存量'
    _COLUMN_BALANCE = '實際庫存'
    
    _COLUMN_DESCRIPTION_1 = '單位'
    _COLUMN_DESCRIPTION_2 = '品名規格'
    
    _SHEETNAME_OUTPUT = '實際庫存'
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tables_1: Dict[str, Table] = None
        self.tables_2: Dict[str, Table] = None
        self.export_table = None
        self.setup_control()
    
    def setup_control(self):
        self.ui.openFileButton_1.clicked.connect(self._open_file_1) 
        self.ui.openFileButton_2.clicked.connect(self._open_file_2)
        self.ui.mappingButton.clicked.connect(self._do_mapping)
        self.ui.saveFileButton.clicked.connect(self._save_file) 
         
    def _open_file_1(self):
        filename, filetype = QFileDialog.getOpenFileName(
            self, 
            self._DISPLAY_OPEN_FILE,
            "./") # start path
        print('open file 1:{}'.format(filename))
        self.ui.showOpenFile_1.setText(filename)
        self._load_table_1(filename)
    
    def _open_file_2(self):
        filename, filetype = QFileDialog.getOpenFileName(
            self, 
            self._DISPLAY_OPEN_FILE,
            "./") # start path
        print('open file 2:{}'.format(filename))
        self.ui.showOpenFile_2.setText(filename)
        self._load_table_2(filename)
    
    def _save_file(self):
        if self.export_table is None:
            return # do nothing
        filename, filetype = QFileDialog.getSaveFileName(self, self._DISPLAY_SAVE_FILE)
        filename = filename if filename.endswith('.xlsx') else '{}.xlsx'.format(filename)
        print('save as {}'.format(filename))
        self.export_table.to_excel(filename, sheet_name=self._SHEETNAME_OUTPUT)

    def _load_table_1(self, excel_file_path):
        self.tables_1: Dict[str, Table] = ExcelLoader(
            excel_file_path, 
            header = self._TABLE_1_HEADER
            ).get_tables()
        for (sheet_name, table) in self.tables_1.items():
            qListWidgetItem: QListWidgetItem = QListWidgetItem(sheet_name)
            self.ui.sheetNames_1.addItem(qListWidgetItem)
        self.ui.sheetNames_1.itemClicked.connect(self._click_sheet_in_table1)
        TableWidgetCreator().fill(table, self.ui.tableWidget_1)
    
    def _load_table_2(self, excel_file_path_2): 
        self.tables_2: Dict[str, Table] = ExcelLoader(
            excel_file_path_2,
            header = self._TABLE_2_HEADER
            ).get_tables()
        for (sheet_name, table) in self.tables_2.items():
            qListWidgetItem: QListWidgetItem = QListWidgetItem(sheet_name)
            self.ui.sheetNames_2.addItem(qListWidgetItem)
        self.ui.sheetNames_2.itemClicked.connect(self._click_sheet_in_table2)
        TableWidgetCreator().fill(table, self.ui.tableWidget_2)

    def _click_sheet_in_table1(self, item):
        table = self.tables_1.get(item.text())
        TableWidgetCreator().fill(table, self.ui.tableWidget_1)
    
    def _click_sheet_in_table2(self, item):
        table = self.tables_2.get(item.text())
        TableWidgetCreator().fill(table, self.ui.tableWidget_2)

    def _do_mapping(self):
        if self.tables_1 is None or self.tables_2 is None:
            return # do nothing
        base_df = DataFrame()
        for table in self.tables_2.values():
            base_df = pd.concat([base_df, table.get_df()], ignore_index=True)
        # reversed find possible primary key
        for table in self.tables_1.values():
            for (idx, row_series) in table.iterrows():
                id = row_series[self._COLUMN_ID]
                amount = row_series[self._COLUMN_AMOUNT_TABLE1]
                if type(amount) == int and (id in base_df[self._COLUMN_ID].unique()) == False:
                    print('need append data from table 1 which is lacked in table 2:{}'.format(id))
                    row_idx = base_df.shape[0]
                    base_df.loc[row_idx] = [None for i in range(base_df.shape[1])]
                    base_df.loc[row_idx, self._COLUMN_ID] = id
                    base_df.loc[row_idx, self._COLUMN_AMOUNT_TABLE2] = 0
                    base_df.loc[row_idx, self._COLUMN_DESCRIPTION_2] = row_series[self._COLUMN_DESCRIPTION_2]

        # add base column
        exported_df = DataFrame()
        exported_df[self._COLUMN_ID] = base_df[self._COLUMN_ID]
        exported_df[self._COLUMN_AMOUNT_TABLE2] = base_df[self._COLUMN_AMOUNT_TABLE2]
        exported_df[self._COLUMN_DESCRIPTION_1] = base_df[self._COLUMN_DESCRIPTION_1]
        exported_df[self._COLUMN_DESCRIPTION_2] = base_df[self._COLUMN_DESCRIPTION_2]

        # remaining balance
        remaining_df = exported_df.copy(deep=True)

        for sheet_name, table in self.tables_1.items():
            df = table.get_df()
            partial_df = DataFrame(index=[])
            partial_df[self._COLUMN_ID] = df[self._COLUMN_ID]
            partial_df[self._COLUMN_AMOUNT_TABLE1] = df[self._COLUMN_AMOUNT_TABLE1]
            partial_df.dropna(subset=[self._COLUMN_ID], inplace=True)
            mapping = dict(partial_df[[self._COLUMN_ID, self._COLUMN_AMOUNT_TABLE1]].values)
            exported_df[sheet_name] = exported_df[self._COLUMN_ID].map(mapping)
            remaining_df[self._COLUMN_AMOUNT_TABLE2] = remaining_df[self._COLUMN_AMOUNT_TABLE2].subtract(exported_df[sheet_name], fill_value=0)

        exported_df[self._COLUMN_BALANCE] = remaining_df[self._COLUMN_AMOUNT_TABLE2]
        exported_df.set_index(self._COLUMN_ID, inplace = True, drop = True)
        exported_df.reset_index(inplace=True)
        exported_df.sort_index()
        self.export_table = exported_df
        TableWidgetCreator().fill(Table(exported_df), self.ui.exportedTableWidget)
