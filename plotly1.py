#!/usr/bin/env python3

import math
# sudo pip install plotly
import plotly
import plotly.graph_objs as go

def plotly_plot(plot_title, xdata, ydata):
    plotly.offline.plot({"data": [go.Scatter(x=xdata, y=ydata)], "layout": go.Layout(title=plot_title) }, 
           auto_open=True)

def my_plot (title, func, x_min, x_max):
    xarray=[]
    yarray=[]
    step = (x_max - x_min)/1000
    for i in range(0, 1000):
        x = x_min + step * i
        y = func(x)
        xarray.append(x)
        yarray.append(y)
    plotly_plot(title, xarray, yarray)     

def my_func(x):
    return math.sin(x) * x

my_plot("x*sin(x)", my_func, 0, 100*math.pi)

  
