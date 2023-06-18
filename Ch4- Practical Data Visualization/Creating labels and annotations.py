import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 8, 4

""""

Labeling plot features

"""
# Functional method
x = range(1, 10)
y = [1, 2, 3, 4, 0.5, 4, 3, 2, 1]
plt.bar(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.show()

z= [1,2,3,4,0.5]
veh_type = ['bicycle', 'motorbike', 'car', 'van', 'stroler']
plt.pie(z, labels=veh_type)
plt.show()

# Object-oriented method
address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 1,1 ])

mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize = 'medium')
ax.set_title('Miles per galon of cars in mtcars dataset')

ax.set_xlabel('car names')
ax.set_ylabel('Miles per gallon')

plt.show()
""""

Adding legend to the plot

"""
plt.pie(z)
plt.legend(veh_type, loc='best')
plt.show()

# Object-oriented method
address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 1,1 ])

mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize = 'medium')
ax.set_title('Miles per galon of cars in mtcars dataset')

ax.set_xlabel('car names')
ax.set_ylabel('Miles per gallon')

ax.legend(loc='best')
plt.show()

""""

Annotating your plot

"""
mpg.max()
ig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 1,1 ])

mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize = 'medium')
ax.set_title('Miles per galon of cars in mtcars dataset')

ax.set_xlabel('car names')
ax.set_ylabel('Miles per gallon')

ax.legend(loc='best')
ax.set_ylim([0,45])
ax.annotate('toyota corolla', xy=(19,33.9), xytext= (21,35), arrowprops=
            dict(facecolor='black', shrink = '0.05'))
plt.show()