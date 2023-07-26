import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression

warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)



lm = LinearRegression()

print("\n")
# Question #1 b):
# Train the model using "engine-size"
# as the independent variable and "price" as the dependent variable?

X = df[['engine-size']]
Y = df['price']

lm.fit(X, Y)

Yhat= lm.predict(X)

print(Yhat[0:4],"\n")


# Write your code below and press Shift+Enter to execute
print(lm.intercept_)


print(lm.coef_)

