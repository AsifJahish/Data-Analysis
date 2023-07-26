import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression

warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)

X = df[['highway-mpg']]
Y = df['price']

lm = LinearRegression()
lm.fit(X, Y)



Yhat=lm.predict(X)
print(Yhat[0:5])

for i in range (10):
    print(Yhat[i])

print("\n")

print(lm.intercept_)
print(df.head())
