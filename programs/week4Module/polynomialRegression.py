import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
import seaborn as sns

from sklearn.preprocessing import PolynomialFeatures

warnings.filterwarnings('ignore')

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"
df = pd.read_csv(filename, header=0)

lm = LinearRegression()

x = df['highway-mpg']
y = df['price']

f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)

def PlotPolly(model, independent_variable, dependent_variable, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

PlotPolly(p, x, y, 'highway-mpg')

pr=PolynomialFeatures(degree=2)
print(pr)

Z_pr=pr.fit_transform(Z)
print(Z.shape)
