# -*- coding: utf-8 -*-
from pandas import DataFrame

class Table():
    
    # just a data frame wrapper here
    df = None

    def __init__(self, dataframe:DataFrame):
        self.df = dataframe
        # default value for null data
        self.df.fillna('', inplace=True)
    
    def row_cnt(self):
        return self.df.shape[0] 
    
    def col_cnt(self):
        return self.df.shape[1]    

    def iterrows(self):
        return self.df.iterrows()
    
    def head(self):
        return self.df.head()