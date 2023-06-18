import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 5, 4


address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\Superstore-Sales.csv"

df = pd.read_csv(address, index_col='Order Date', encoding='cp1252', parse_dates=True)
print(df.head())

df['Order Quantity'].plot()
plt.show()

df2 = df.sample(n=100, random_state=25, axis=0)
plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()
plt.show()