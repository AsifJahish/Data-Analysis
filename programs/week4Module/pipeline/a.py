
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import seaborn as sns



# regression Plot ? we use scatter plot also the the linear regression line to show the module
warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]


pr=PolynomialFeatures(degree=2)
Z_pr=pr.fit_transform(Z)
print(Z.shape)
print(Z_pr.shape)

