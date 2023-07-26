import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())

# Create a 1x3 grid of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot the first scatter plot (engine-size vs. price)
sns.regplot(x="engine-size", y="price", data=df, ax=axes[0])
axes[0].set_ylim(0,)
axes[0].set_title("Engine Size vs. Price")

# Plot the second scatter plot (highway-mpg vs. price)
sns.regplot(x="highway-mpg", y="price", data=df, ax=axes[1])
axes[1].set_title("Highway MPG vs. Price")

# Plot the third scatter plot (peak-rpm vs. price)
sns.regplot(x="peak-rpm", y="price", data=df, ax=axes[2])
axes[2].set_title("Peak RPM vs. Price")

# Display all three scatter plots side by side
plt.tight_layout()
plt.show()

# Calculate and print correlation between "highway-mpg" and "price"
correlation1 = df[['highway-mpg', 'price']].corr()
print(correlation1)
