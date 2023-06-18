import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

import seaborn as sb
sb.set_style('whitegrid')

address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

cars.index = cars.car_names

mpg = cars['mpg']

mpg.plot(kind='hist')
plt.show()


plt.hist(mpg)
plt.plot()
plt.show()


sb.displot(mpg)
cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgray'], s=150)
sb.regplot(x='hp', y='mpg', data=cars, scatter=True)
plt.show()

# Generating a scatter plot matrix
sb.pairplot(cars)

cars_subset = cars[['mpg', 'disp', 'hp', 'wt']]
sb.pairplot(cars_subset)
plt.show()

# Building boxplot
cars.boxplot(column='mpg', by='am')
cars.boxplot(column='wt', by='am')
plt.show()

# with seaborn
sb.boxplot(x='am', y='mpg', data=cars, palette='hls')