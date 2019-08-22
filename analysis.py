import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.io import output_file, output_notebook
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from sklearn.linear_model import LinearRegression
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import MaxNLocator
from scipy import stats
import scipy as sp


# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# dates = pd.date_range('20130101',periods=6)
# # print(dates)

data = pd.read_csv('data.csv')
X = data.iloc[:, 0].values.reshape(-1, 1)
Y = data.iloc[:, 1].values.reshape(-1, 1)

slope, intercept, r_value, p_value, std_err = sp.stats.mstats.linregress(X,Y)

linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

print('r',r_value)
print('slope',slope)
print('intercept',intercept)


plt.scatter(X, Y)

plt.plot(X, Y_pred, color='red')
plt.show()

def thing():
  return 'hi'

print(thing())