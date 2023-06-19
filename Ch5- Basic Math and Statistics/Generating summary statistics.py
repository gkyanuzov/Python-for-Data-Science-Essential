import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats



address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']


""""

Summary statistics that describe a variables numeric values

"""
# print(cars.sum())
# # print(cars.sum(axis=1))
#
# print(cars.median())
#
# cars.mean()
# cars.max()
# print(cars.min())

mpg = cars.mpg

print(mpg.idxmax())


""""

Summary statistics that describe variables distribution

"""
#
# print(cars.std())
# print(cars.var())

gear = cars.gear
print(gear.value_counts())

print(cars.describe())