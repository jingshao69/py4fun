#!/usr/bin/python

from scipy.stats import norm
import math
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
    return norm.pdf(x)

x_min = norm.ppf(0.01)
x_max = norm.ppf(0.99)
print(x_min, x_max)
my_plot("normal distribution", my_func, norm.ppf(0.01), norm.ppf(0.99))

  
