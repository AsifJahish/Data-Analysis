import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())

# ANOVA: Analysis of Variance
# The Analysis of Variance (ANOVA) is a statistical method used to test whether
# there are significant differences between the means of two or more groups. ANOVA returns two parameters:
#
# F-test score: ANOVA assumes the means of all groups are the same, calculates how much the actual means deviate
# from the assumption, and reports it as the F-test score. A larger score means there is a larger difference between the means.
#
# P-value: P-value tells how statistically significant our calculated score value is.
#
# If our price variable is strongly correlated with the variable we are analyzing, we expect ANOVA to return a sizeable F-test score and a small p-value.
#
# Drive Wheels
# Since ANOVA analyzes the difference between different groups of the same variable, the groupby function will come in handy. Because the ANOVA algorithm averages the data automatically, we do not need to take the average before hand.
#
# To see if different types of 'drive-wheels' impact 'price', we group the data.
grouped_test2 = df[['drive-wheels', 'price']].groupby(['drive-wheels'])
print(grouped_test2.head(2))

print(grouped_test2.get_group('4wd')['price'])

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'],
                              grouped_test2.get_group('4wd')['price'])

print("ANOVA results: F=", f_val, ", P =", p_val)

# Name: price, dtype: float64
# ANOVA results: F= 67.95406500780399 , P = 3.3945443577151245e-23