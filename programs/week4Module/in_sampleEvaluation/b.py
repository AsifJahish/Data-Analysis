import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.metrics import mean_squared_error


# regression Plot ? we use scatter plot also the linear regression line to show the module
warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)

lm = LinearRegression()

X = df['horsepower'].values.reshape(-1, 1)  # Reshape X into a 2D array with a single column
Y = df['price']


lm.fit(X, Y)
# Find the R^2
print('The R-square is: ', lm.score(X, Y))

Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])

mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)
