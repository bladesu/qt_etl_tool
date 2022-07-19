# -*- coding: utf-8 -*-
from misc import AggregateFunctionType, AggregateDimension

class AggregateOperation:
    
    _agg_type: AggregateFunctionType
    _agg_dimension: AggregateDimension
    _agg_method: lambda x: x
    
    def __init__(self, 
                 agg_type: AggregateFunctionType,
                 agg_dimension: AggregateDimension,
                 agg_method
                 ):
        self._agg_type = agg_type
        self._agg_dimension = agg_dimension
        self._agg_method = agg_method
        
    @property
    def agg_type(self):
       return self._agg_type

    @agg_type.setter
    def agg_type(self, value: AggregateFunctionType):
        self._agg_type = value
    
    @property
    def agg_dimension(self):
       return self._agg_dimension

    @agg_dimension.setter
    def agg_dimension(self, value: AggregateDimension):
        self._agg_dimension = value
 
    @property
    def agg_method(self):
       return self._agg_method

    @agg_method.setter
    def agg_method(self):
        self.agg_method = value