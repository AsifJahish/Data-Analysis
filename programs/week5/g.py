import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Import clean data
df = pd.read_csv("/home/asifjahish/DataAnalysis/venv/data/module_5_auto.csv")

# Separate the target variable 'price' from the features
# ... (Code for importing and preparing the data, as you provided)

# Create a LinearRegression object and fit the model on the original training set
lre = LinearRegression()
lre.fit(x_train[['horsepower']], y_train)

# Calculate the R-squared score on the original test set
r2_test_original = lre.score(x_test[['horsepower']], y_test)
print("R-squared score (original test set):", r2_test_original)

# Calculate the R-squared score on the new test set (x_test1, y_test1)
r2_test_new = lre.score(x_test1[['horsepower']], y_test1)
print("R-squared score (new test set):", r2_test_new)
