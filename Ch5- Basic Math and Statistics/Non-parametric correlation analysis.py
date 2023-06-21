import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import pearsonr, spearmanr

rcParams['figure.figsize'] = 14, 7
plt.style.use('seaborn-whitegrid')

""""

The Spearman Rank Correlation

"""
address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

print(cars.head())
# sb.pairplot(cars)

X = cars[['cyl', 'vs', 'am', 'gear']]
# sb.pairplot(X)
plt.show()

cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']

spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print("Spearman RAnk Correlation Coefficient %0.3f" % (spearmanr_coefficient))

spearmanr_coefficient, p_value = spearmanr(cyl, am)
print("Spearman RAnk Correlation Coefficient %0.3f" % (spearmanr_coefficient))
spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print("Spearman RAnk Correlation Coefficient %0.3f" % (spearmanr_coefficient))

""""

Chi-Square test for independence

"""
table = pd.crosstab(cyl, am)
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

table = pd.crosstab(cyl, vs)
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

table = pd.crosstab(cyl, gear)
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

# p values are smaller than 0.05 => values are correlated
