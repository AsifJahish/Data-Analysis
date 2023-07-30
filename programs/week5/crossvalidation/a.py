from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import pandas as pd

# Import clean data
df = pd.read_csv("/home/asifjahish/DataAnalysis/venv/data/module_5_auto.csv")

# Separate the target variable 'price' from the features
y_data = df['price']
x_data = df.drop('price', axis=1)

# Create a LinearRegression object
lre = LinearRegression()

# Perform 4-fold cross-validation on the linear regression model using 'horsepower' as the feature
Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4)

# Calculate the mean and standard deviation of the cross-validated R-squared scores
mean_r2 = Rcross.mean()
std_r2 = Rcross.std()

print("Mean R-squared score:", mean_r2)
print("Standard deviation of R-squared scores:", std_r2)

# Perform cross-validation to compute negative mean squared error
neg_mse = -1 * cross_val_score(lre, x_data[['horsepower']], y_data, cv=4, scoring='neg_mean_squared_error')

print("Negative mean squared error:", neg_mse)

Rc=cross_val_score(lre,x_data[['horsepower']], y_data,cv=2)
Rc.mean()

# Standard deviation of R-squared scores: 0.291183944475603
# Negative mean squared error: [20254142.84026702 43745493.2650517  12539630.34014931 17561927.72247591]

