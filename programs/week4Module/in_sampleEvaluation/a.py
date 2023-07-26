#
# 4. Measures for In-Sample Evaluation
# When evaluating our models, not only do we want to
# visualize the results, but we also want a quantitative measure to determine how accurate the model is.
#
# Two very important measures that are often used in Statistics to determine the accuracy of a model are:
#
# R^2 / R-squared
# Mean Squared Error (MSE)
# R-squared
#
# R squared, also known as the coefficient of determination, is a measure to indicate how close the data is to the fitted regression line.
#
# The value of the R-squared is the percentage of variation of the response variable (y) that is explained by a linear model.
#
# Mean Squared Error (MSE)
#
# The Mean Squared Error measures the average of the squares of errors. That
# is, the difference between actual value (y) and the estimated value (ŷ).

#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
import seaborn as sns

# regression Plot ? we use scatter plot also the linear regression line to show the module
warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)

lm = LinearRegression()

X = df['horsepower'].values.reshape(-1, 1)  # Reshape X into a 2D array with a single column
Y = df['price']

# highway_mpg_fit
lm.fit(X, Y)

# Find the R^2
print('The R-square is:', lm.score(X, Y))

Yhat = lm.predict(X)
print('The output of the first four predicted values is:', Yhat[0:4])

sns.lmplot(x='horsepower', y='price', data=df)

# Show the plot
plt.show()
