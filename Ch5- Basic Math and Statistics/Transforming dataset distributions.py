import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams
import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

rcParams['figure.figsize'] = 5, 4
plt.style.use('seaborn-whitegrid')

address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg
plt.plot(mpg)
plt.show()

print(cars[['mpg']].describe())

mpg_matrix = mpg.values.reshape(-1, 1)
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
plt.show()

scaled = preprocessing.MinMaxScaler(feature_range=(0, 10))
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
plt.show()

# using scale() to scale features
standartized_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)
plt.plot(standartized_mpg)
plt.show()

standartized_mpg = scale(mpg)
plt.plot(standartized_mpg)
plt.show()
