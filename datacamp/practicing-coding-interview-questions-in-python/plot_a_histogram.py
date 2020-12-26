'''
Instructions
- Plot a simple histogram of the plasma retinol feature.
- Redefine the histogram to have 20 bins.
- Add a title to the plot (choose any name you want).
- Add other missing parts to the plot.
'''

# Plot a simple histogram of the plasma retinol feature
plt.hist(retinol['plasma retinol'])
plt.show()

# Redefine the histogram to have 20 bins
plt.hist(retinol['plasma retinol'], bins=20)
plt.show()

# Add a title to the plot
plt.title('Histogram of Plasma Retinol')
plt.show()

# Add other missing parts to the plot
plt.xlabel("Xlabel")
plt.ylabel("Ylabel")
plt.show()