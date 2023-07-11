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

""""

Line Charts


"""

# a very basic line chart
a = np.linspace(start=0, stop=36, num=36)
np.random.seed(25)

b = np.random.uniform(low=0.0, high=1.0, size=36)

trace = go.Scatter(x=a, y=b)

data = [trace,]

# a line chart from pandas df
address = r"D:\Docs\Uni\Online Courses\Python for Data Science Essential Training Part 1 - " \
          "LinkedInLearning\Ex_Files_Python_Data_Science_EssT_Pt_1\Exercise Files\Data\mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', "qsec", 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'wt', 'mpg']]

layout = dict(title='Chart from pandas df', xaxis=dict(title='x-axis'),
              yaxis=dict(title='ý-axis'))

# df.iplot(filename='cfsimplelinechart', layout =layout)

""""

Bar charts

"""
data1 = [go.Bar(x=[1,2,3,4,5,6,7,8,9,10], y=[1,2,3,4,0.5,4,3,2,1])]
print(data1)
layout1 = dict(title = 'Simple Bar chart',
               xaxis=dict(title='x-axis'),
               yaxis=dict(title='ý-axis'))
# cs.iplot(data1, filename='basicbarchart', layout= layout1)

""""

Creating pie chart

"""

fig = {'data': [{'labels': ['bicycle', 'motorcycle', 'car', 'van', 'stroller'],
                 'values': [1,2,3,4,0.5],
                 'type': 'pie'}],
       'layout':{'title': 'Pie Chart'}}

# cs.iplot(fig)



