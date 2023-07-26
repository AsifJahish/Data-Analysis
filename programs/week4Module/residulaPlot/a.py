# Residual Plot
# A good way to visualize the variance of the data is to use a residual plot.
#
# What is a residual?
#
# The difference between the observed value (y) and the predicted value (Yhat
# ) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to
# the fitted regression line.
#
# So what is a residual plot?
#
# A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.
#
# What do we pay attention to when looking at a residual plot?
#
# We look at the spread of the residuals:
#
# - If the points in a residual plot are randomly spread out around the x-axis, then a linear model is appropriate for the data.
#
# Why is that? Randomly spread out residuals means that the variance is constant, and thus the linear model is a good fit for this data.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression

import seaborn as sns



# regression Plot ? we use scatter plot also the the linear regression line to show the module
warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(x=df['highway-mpg'],y=df['price'])
plt.show()
