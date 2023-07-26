# Continuous Numerical Variables:¶
# Continuous numerical variables are variables that may
# contain any value within some range. They can be of type "int64" or "float64". A great way to visualize
# these variables is by using scatterplots with fitted lines.
#
# In order to start understanding the (linear) relationship between an individual variable
# and the price, we can use "regplot" which plots the scatterplot plus
# the fitted regression line for the data.
#


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())

# sns.regplot(x="engine-size", y="price", data=df)
# plt.ylim(0,)
# plt.show()

correlation= df[["engine-size", "price"]].corr()

print(correlation)

sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()



sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()

correlation1= df[['highway-mpg', 'price']].corr()
print(correlation1)



