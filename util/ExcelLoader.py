# -*- coding: utf-8 -*-

from typing import Dict
import pandas as pd
from model.Table import Table

# modify from https://learndataanalysis.org/source-code-how-to-import-excel-data-to-a-qtablewidget-pyqt6-tutorial/

class ExcelLoader(object):
    
    def __init__(self, excel_file_path = None , worksheet_name = None, header = None):
        super().__init__()
        self._excel_file_path = excel_file_path 
        self._worksheet_name = worksheet_name
        self._header = header
    
    def get_table(self):
        return Table(pd.read_excel(self._excel_file_path, sheet_name=self._worksheet_name, header= self._header))
    
    def get_tables(self) -> dict:
        tables: Dict = pd.read_excel(self._excel_file_path, sheet_name=None, header= self._header)
        newMap = {}
        for (sheet_name, table_data) in tables.items():
            newMap[sheet_name] = Table(table_data) 
        return newMap