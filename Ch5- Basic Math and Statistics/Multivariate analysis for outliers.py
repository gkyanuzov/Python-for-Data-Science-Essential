import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import  seaborn as sb

rcParams['figure.figsize'] = 5, 4
plt.style.use('seaborn-whitegrid')


rcParams['figure.figsize'] = 5, 4
address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\iris.data.csv"

df = pd.read_csv(filepath_or_buffer=address, header=None, sep=',')
df.columns = ['Sepal Length', 'Sepal width', 'Petal Length', 'Petal Width', 'Species']

data = df.iloc[:, 0:4].values
target = df.iloc[:,4].values

sb.boxplot(x='Species', y='Sepal Length', data=df, palette='hls')
plt.show()


#scatterplot matrix

sb.pairplot(df, hue='Species', palette='hls')
plt.show()