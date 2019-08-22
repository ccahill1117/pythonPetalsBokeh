import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.io import output_file, output_notebook
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# dates = pd.date_range('20130101',periods=6)
# # print(dates)

# df = pd.DataFrame(np.random.randn(6, 6), index=dates, columns=list('ABCDEF'))
# print(df.head(2))
# print(df.tail(2))

# print(df)

# df2 = pd.DataFrame({'A': 1.,
#                         'B': pd.Timestamp('20130102'),
#                         'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                         'D': np.array([3] * 4, dtype='int32'),
#                         'E': pd.Categorical(["test", "train", "test", "train"]),
#                         'F': 'foo'})
# # print(df2)
# print(df2.dtypes)

# data = {
#   'apples': [0,1,2,3],
#   'cars': [9,8,7,43]
# }
# print(pd.DataFrame(data))

# df = pd.DataFrame({
#                       # 'A': ['one', 'one', 'two', 'three'] * 3,
#                       # 'B': ['A', 'B', 'C'] * 4,
#                       # 'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
#                       'D': (np.absolute(np.random.randn(30))),
#                       'E': (np.absolute(np.random.randn(30)))})
# print(df)     

# dff = pd.Series(
#                       # 'A': ['one', 'one', 'two', 'three'] * 3,
#                       # 'B': ['A', 'B', 'C'] * 4,
#                       # 'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
#                       (np.absolute(np.random.randn(30))),
#                       (np.absolute(np.random.randn(30))))

x = [5,4,3,2]
y = [1,2,3,4]

fig = figure(background_fill_color='gray',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
             plot_height=300,
             plot_width=500,
             h_symmetry=True,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             y_range=(0, 10),
             x_range=(0, 10),
             title='Example Figure',
             title_location='right',
             toolbar_location='below',
             tools='save')

fig.circle(x=x,y=y,
          color='red', size=12, alpha=0.5)             

show(fig)             



# p.circle(x, y, size=10, color='red', legend='circle')
# p.line(x, y, color='blue', legend='line')
# p.triangle(y, x, color='gold', size=10, legend='triangle')

# output_file('my_first_graph.html')

def thing():
  return 'hi'

print(thing())