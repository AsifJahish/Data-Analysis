import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from ipywidgets import interact, interactive, fixed, interact_manual

# Import clean data
df = pd.read_csv("/home/asifjahish/DataAnalysis/venv/data/module_5_auto.csv")

df = df._get_numeric_data()
print(df.head())

# Assuming you have columns named 'city-mpg' and 'highway-mpg' that you want to compare
city_mpg_data = df['city-mpg']
highway_mpg_data = df['highway-mpg']


def PollyPlot(xtrain, xtest, y_train, y_test, lr, poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    # training data
    # testing data
    # lr:  linear regression object
    # poly_transform:  polynomial transformation object

    xmax = max([xtrain.values.max(), xtest.values.max()])

    xmin = min([xtrain.values.min(), xtest.values.min()])

    x = np.arange(xmin, xmax, 0.1)

    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()

DistributionPlot(city_mpg_data, highway_mpg_data, "City MPG", "Highway MPG", "Distribution of City MPG and Highway MPG")
