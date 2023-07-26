
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


new_input=np.arange(1, 100, 1).reshape(-1, 1)

lm.fit(X, Y)

print(lm, "\n")

yhat=lm.predict(new_input)
print(yhat[0:5])

plt.plot(new_input, yhat)
plt.show()