import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import pearsonr

# data visualization size
rcParams['figure.figsize'] = 8, 4
plt.style.use('seaborn-whitegrid')

""""

The Pearson Correlation

"""
# uncovers relationships between variables

address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

# sb.pairplot(cars)
plt.show()

X = cars[['mpg', 'hp', 'qsec', 'wt']]
# sb.pairplot(X)
plt.show()


""""

Using scipy to calcualte Pearson correlation coefficitnt

"""


mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']


pearsonr_coefficient, p_value = pearsonr(mpg, hp)
print('PearsonR correlation coefficient %0.3f'% (pearsonr_coefficient))

pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print('PearsonR correlation coefficient %0.3f'% (pearsonr_coefficient))

pearsonr_coefficient, p_value = pearsonr(mpg, wt)

print('PearsonR correlation coefficient %0.3f'% (pearsonr_coefficient))

# Using pandas to calculate the Pearson correlation coefficient
corr = X.corr()
print(corr)

# Using seaborn to calculate the Pearson correlation coefficient
sb.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show()