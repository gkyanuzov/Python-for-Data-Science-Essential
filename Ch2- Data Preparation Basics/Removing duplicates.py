import numpy as np
import pandas as pd

from pandas import Series, DataFrame

""""

Removing duplicates

"""
DF_obj = DataFrame({'column 1': [1,1,2,2,3,3,3],
                    'column2': ['a', 'a', 'b','b', 'c', 'c', 'c'],
                    'column3': ["A", "A", "B", "B", "C", "C", "C"]})
print(DF_obj)

print(DF_obj.duplicated())

print(DF_obj.drop_duplicates())

DF_obj = DataFrame({'column 1': [1,1,2,2,3,3,3],
                    'column2': ['a', 'a', 'b','b', 'c', 'c', 'c'],
                    'column3': ["A", "A", "B", "B", "C", "D", "C"]})

print(DF_obj.drop_duplicates(['column3']))