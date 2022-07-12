# -*- coding: utf-8 -*-

import pandas as pd
from model.Table import Table

# modify from https://learndataanalysis.org/source-code-how-to-import-excel-data-to-a-qtablewidget-pyqt6-tutorial/

class ExcelLoader(object):
    
    _excel_file_path = ''
    _worksheet_name = ''

    def __init__(self, excel_file_path, worksheet_name):
        super().__init__()
        self._excel_file_path = excel_file_path 
        self._worksheet_name = worksheet_name
    
    def get_table(self):
        return Table(pd.read_excel(self._excel_file_path, sheet_name=self._worksheet_name))