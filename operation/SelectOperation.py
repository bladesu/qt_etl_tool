from model.Table import *

class SelectOperation:
    
    def __init__(self, 
                 from_table:Table,
                 where_i:int,
                 where_j:int
                 ):
        self.table = from_table
        self.i = where_i
        self.j = where_j
        
    def get(self):
        return self.table.get(self.i, self.j)