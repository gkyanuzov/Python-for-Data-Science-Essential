import IPython.display
import numpy as np
import pandas as pd
import cufflinks as cf
import chart_studio.plotly as py
import chart_studio as cs
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.offline
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode()
import sklearn
from sklearn.preprocessing import StandardScaler

""""

Creating histograms

"""
# make a histogram form pandas Series
address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

mpg = cars._is_homogeneous_type

    # mpg.iplot(kind='histogram', filename='simple-hsitogram0chart')

# multiple histogram
cars_subset = cars[['mpg', 'disp', 'hp']]
cars_data_std = StandardScaler().fit_transform(cars_subset)

cars_select = pd.DataFrame(cars_data_std)
cars_select.columns = ['mpg', 'disp', 'hp']

    # cars_select.iplot(kind='histogram', filename='multiple-histogramchart')

#subplot histogram
    # cars_select.iplot(kind='histogram', filename='subplot-histogramchart, subplots=True')


""""

Creating box plots

"""
# cars_select.iplot(kind='box', filename='subplot-boxplots')

""""

Creating scatter plots

"""
fig = {'data':[{'x': cars_select.mpg, 'y': cars_select.disp, 'mode': 'markers', 'name': 'mpg'},
               {'x': cars_select.hp, 'y': cars_select.disp, 'mode': 'markers', 'name': 'hp'}, ]}

# cars_select.iplot(kind='scatter', filename='scatterplots')






