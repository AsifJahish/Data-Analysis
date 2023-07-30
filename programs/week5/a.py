import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed, interact_manual

# Import clean data
df = pd.read_csv("/home/asifjahish/DataAnalysis/venv/data/module_5_auto.csv")

df = df._get_numeric_data()

# Assuming you have columns named 'city-mpg' and 'highway-mpg' that you want to compare
city_mpg_data = df['city-mpg']
highway_mpg_data = df['highway-mpg']

def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    ax1 = sns.distplot(RedFunction, hist=False, color="r", label=RedName)
    ax2 = sns.distplot(BlueFunction, hist=False, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Miles per Gallon (MPG)')
    plt.ylabel('Proportion of Cars')

    plt.show()
    plt.close()

# Call the function with 'city-mpg' and 'highway-mpg' data
DistributionPlot(city_mpg_data, highway_mpg_data, "City MPG", "Highway MPG", "Distribution of City MPG and Highway MPG")
