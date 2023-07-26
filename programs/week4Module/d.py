


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression

warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)



lm = LinearRegression()


Z = df[['normalized-losses', 'highway-mpg']]
Y = df['price']

lm.fit(Z, Y)

Yhat = lm.predict(Z)

Yhat = lm.predict(Z)
print(Yhat[0:5])

# Find the coefficient of the model.
print("Intercept:", lm.intercept_)
print("Coefficients:", lm.coef_)
