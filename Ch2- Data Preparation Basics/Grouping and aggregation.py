import numpy as np
import pandas as pd

from pandas import Series, DataFrame

""""

Grouping data by column index

"""

address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)

cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec",'vs', 'am', 'gear', 'carb']

print(cars.head())

cars_groups = cars.groupby(cars['cyl'])
print(cars_groups)
