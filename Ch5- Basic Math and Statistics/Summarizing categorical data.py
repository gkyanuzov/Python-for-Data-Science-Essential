import numpy as np
import pandas as pd


address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names
print(cars.head(15))

carb = cars.carb
print(carb.value_counts())

cars_cat = cars[['cyl', 'vs','am','gear', 'carb']]
print(cars_cat.head())

gears_group = cars_cat.groupby('gear')
print(gears_group.describe())


""""

Transforming variables to categorical data type

"""
cars['group'] = pd.Series(cars.gear,dtype='category')
print(cars['group'])
print(cars['group'].dtypes)

print(cars['group'].value_counts())



print(pd.crosstab(cars['am'], cars['gear']))
