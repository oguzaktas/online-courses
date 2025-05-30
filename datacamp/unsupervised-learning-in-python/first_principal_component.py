'''
Instructions
- Make a scatter plot of the grain measurements. This has been done for you.
- Create a PCA instance called model.
- Fit the model to the grains data.
- Extract the coordinates of the mean of the data using the .mean_ attribute of model.
- Get the first principal component of model using the .components_[0,:] attribute.
- Plot the first principal component as an arrow on the scatter plot, using the plt.arrow() function. 
You have to specify the first two arguments - mean[0] and mean[1].
'''

# Import necessary modules
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Make a scatter plot of the untransformed points
plt.scatter(grains[:,0], grains[:,1])

# Create a PCA instance: model
model = PCA()

# Fit model to points
model.fit(grains)

# Get the mean of the grain samples: mean
mean = model.mean_

# Get the first principal component: first_pc
first_pc = model.components_[0,:]

# Plot first_pc as an arrow, starting at mean
plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color='red', width=0.01)

# Keep axes on same scale
plt.axis('equal')
plt.show()
