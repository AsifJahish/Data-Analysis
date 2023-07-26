import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#
# P-value
#
# What is this P-value? The P-value is the probability value that the correlation
# between these two variables is statistically significant. Normally, we choose a significance level of 0.05,
# which means that we are 95% confident that the correlation between the variables is significant.
#
# By convention, when the
#
# p-value is
# <
#   0.001: we say there is strong evidence that the correlation is significant.
# the p-value is
# <
#   0.05: there is moderate evidence that the correlation is significant.
# the p-value is
# <
#   0.1: there is weak evidence that the correlation is significant.
# the p-value is
# >
#   0.1: there is no evidence that the correlation is significant.




filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
# Wheel-Base vs. Price
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)