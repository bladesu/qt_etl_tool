# -*- coding: utf-8 -*-
from numpy import isin
from model.Table import Table
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
import numbers

class TableWidgetCreator(object):
    
    _is_add_header = True
    
    def __init__(self, is_add_header = True):
        self._is_add_header = is_add_header

    def _init_table(self, row, column, qTableWidget: QTableWidget):
        qTableWidget.setRowCount(row)
        qTableWidget.setColumnCount(column)
        qTableWidget.setColumnWidth(2, 300)
    
    def _create_item(self, value):
        if isinstance(value, int):
            value =  '{:10d}'.format(value)
        elif isinstance(value, numbers.Number):
            value =  '{:10.1f}'.format(value)
        return QTableWidgetItem(str(value))
        
    def fill(self, table: Table, qTableWidget: QTableWidget):
        total_row_cnt = table.row_cnt() + 1 if self._is_add_header else table.row_cnt()
        self._init_table(total_row_cnt, table.col_cnt(), qTableWidget)

        first_row_threshold = 0
        # add header
        if self._is_add_header:
            row_index = 0
            first_row_threshold = first_row_threshold + row_index + 1
            for col_index, value in enumerate(table.head()):
                qTableWidget.setItem(row_index, col_index, self._create_item(value))

        # add data row by row
        for row in table.iterrows():
            row_index = row[0] + first_row_threshold
            for col_index, value in enumerate(row[1]):
                qTableWidget.setItem(row_index, col_index, self._create_item(value))
        return qTableWidget
    