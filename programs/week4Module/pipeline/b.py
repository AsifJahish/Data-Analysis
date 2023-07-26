import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import seaborn as sns

# regression Plot ? we use scatter plot also the the linear regression line to show the module
warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"
df = pd.read_csv(filename, header=0)

# Define the predictor variables (X) and the target variable (y)
X = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
y = df['price']

# Create a pipeline with three steps: scaling, polynomial features, and linear regression model
Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]

pipe = Pipeline(Input)

# Fit the pipeline on the data
pipe.fit(X, y)

# Make predictions using the fitted pipeline
ypipe = pipe.predict(X)
print(ypipe[0:4])
