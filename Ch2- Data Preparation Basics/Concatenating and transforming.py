import numpy as np
import pandas as pd

from pandas import Series, DataFrame

DF_obj = DataFrame(np.arange(36).reshape(6, 6))
print(DF_obj)

DF_obj_2 = DataFrame(np.arange(15).reshape(5, 3))
print(DF_obj_2)

""""

Concatenating data

"""

concat_df = pd.concat([DF_obj, DF_obj_2], axis=1)  # concats by adding columns
print(concat_df)

concat_df2 = pd.concat([DF_obj, DF_obj_2])  # concats by adding rows
print(concat_df2)

""""

Transforming data

"""
print(DF_obj.drop([0, 2]))  # drops rows 2 and 0
print(DF_obj.drop([0, 2], axis=1))  # drops columns 2 and 0

""""

Adding data

"""

series_obj = Series(np.arange(6))
series_obj.name = 'added variable'
print(series_obj)

variable_added = DataFrame.join(DF_obj, series_obj)  # joins
print(variable_added)

added_datatable = variable_added._append(variable_added, ignore_index=False)
print(added_datatable)

added_datatable = variable_added._append(variable_added, ignore_index=True)
print(added_datatable)

""""

Sorting data

"""

DF_sorted = DF_obj.sort_values(by=(5), ascending=False)  # sort by values in col 5
print(DF_sorted)
