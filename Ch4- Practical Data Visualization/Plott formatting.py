import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 5, 4

""""

Defining plot color

"""
x = range(1, 10)
y = [1, 2, 3, 4, 0.5, 4, 3, 2, 1]
plt.bar(x, y)
# plt.show()

wide = [0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.5, 0.5, 0.5]
color = ['salmon']
plt.bar(x, y, width=wide, color=color, align='center')
# plt.show()


address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'mpg', 'wt']]
df.plot()
plt.show()

color_theme = ['darkgray', 'lightsalmon', 'powderblue']
df.plot(color=color_theme)
plt.show()

z = [1, 2, 3, 4, 0.5]
plt.pie(z)
plt.show()

color_theme1 =[ '#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
plt.pie(z, colors = color_theme1)
plt.show()

""""

Customizing line styles

"""
x1 = range(0,10)
y1 = [10,9,8,7,6,5,4,3,2,1]

plt.plot(x, y, ds='steps', lw=5)
plt.plot(x1, y1, ls= '--', lw=10)
plt.show()

# Setting plot markers
plt.plot(x, y, marker = '1', mew = 20)
plt.plot(x1, y1, marker= '+', mew = 15)
plt.show()