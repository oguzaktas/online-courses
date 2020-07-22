'''
Instructions
- In the IPython Shell, inspect the DataFrame df using df.head(). This will let you identify 
which column names you need to pass as the x and y keyword arguments in your call to sns.swarmplot().
- Use sns.swarmplot() to make a bee swarm plot from the DataFrame containing the Fisher iris data set, 
df. The x-axis should contain each of the three species, and the y-axis should contain the petal lengths.
- Label the axes.
- Show your plot.
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/iris.csv')

# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
