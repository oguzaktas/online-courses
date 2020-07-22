'''
Instructions - 1
- Start from scratch: import matplotlib.pyplot as plt.
- Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
- Finish the script with plt.show() to actually display the plot. Do you see a correlation?

Instructions - 2
- Change the line plot that's coded in the script to a scatter plot.
- A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').
- Finish off your script with plt.show() to display the plot.
'''

import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()
