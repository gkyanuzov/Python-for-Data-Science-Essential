import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

""""

Creating a line chart from a list object

"""

# Plotting a line chart in matplotlib
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

plt.plot(x, y)

# Plotting a line chort from Pandas object
address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

mpg = cars['mpg']
mpg.plot()

df = cars[['cyl', 'wt', 'mpg']]
df.plot()

""""

Creating bar charts

"""
# from a list
plt.bar(x, y)

# from pandas objects
mpg.plot(kind='bar')

# vertically
mpg.plot(kind='barh')

""""

Creating a pie chart

"""

x = [1, 2, 3, 4, 5]
plt.pie(x)

plt.pie(x)
# save the plot
plt.savefig('Pie_chart.png')
plt.show()
