# Categorical Variables¶
# These are variables that describe a 'characteristic' of a
# data unit, and are selected from a small group of categories.
# The categorical variables
# can have the type "object" or "int64". A good way to visualize categorical variables is by using boxplots.



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Box plot of body-style vs. price
sns.boxplot(x="body-style", y="price", data=df, ax=axes[0])

plt.xlabel("Body Style")
plt.ylabel("Price")
plt.xticks(rotation=45)
axes[0].set_ylim(0,)
axes[0].set_title("Body Style vs. Price")


sns.boxplot(x="engine-location", y="price", data=df, ax=axes[1])

axes[1].set_title("engine location  vs. Price")
plt.show()

# Calculate and print correlation between "body-style" and "price"
correlation = df[["body-style", "price"]].corr()
print(correlation)
