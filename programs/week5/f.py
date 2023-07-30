import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Import clean data
df = pd.read_csv("/home/asifjahish/DataAnalysis/venv/data/module_5_auto.csv")

# Separate the target variable 'price' from the features
y_data = df['price']
x_data = df.drop('price', axis=1)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_data[['horsepower']], y_data, test_size=0.2, random_state=42)

# Create a LinearRegression object and fit the model
lre = LinearRegression()
lre.fit(x_train[['horsepower']], y_train)

# Calculate the R-squared score for the test and training sets
r2_test = lre.score(x_test[['horsepower']], y_test)
r2_train = lre.score(x_train[['horsepower']], y_train)

print("R-squared score (test):", r2_test)
print("R-squared score (train):", r2_train)

# Visualize actual vs. predicted 'price' values for both training and testing sets
plt.figure(figsize=(8, 6))
plt.scatter(x_train['horsepower'], y_train, color='blue', label='Actual (Train)')
plt.scatter(x_test['horsepower'], y_test, color='green', label='Actual (Test)')
plt.plot(x_train['horsepower'], lre.predict(x_train[['horsepower']]), color='red', label='Predicted')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.legend()
plt.show()
