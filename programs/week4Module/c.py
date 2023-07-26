# Multiple Linear Regression
# What if we want to predict car price using more than one variable?
#
# If we want to use more variables in our model to predict car price, we can use Multiple Linear Regression.
# Multiple Linear Regression is very similar to Simple Linear Regression, but this method is used to explain the relationship
# between one continuous response (dependent) variable and two or more predictor (independent) variables. Most of the real-world
# regression models involve multiple predictors. We will illustrate the structure by using four predictor variables, but these
# results can generalize to any integer:
#
#
# From the previous section we know that other good predictors of price could be:
#
# Horsepower
# Curb-weight
# Engine-size
# Highway-mpg
# Let's develop a model using these variables as the predictor variables.









import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression

warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)



lm = LinearRegression()

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

X=df['price']
lm.fit(Z,X)

Yhat=lm.predict(Z)
print(Yhat[0:2])

print("Intercept:", lm.intercept_)
print("Coefficients:", lm.coef_)