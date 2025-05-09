'''
Instructions
- Import scale from sklearn.preprocessing.
- Scale the features X using scale().
- Print the mean and standard deviation of the unscaled features X, and then the scaled features X_scaled. 
Use the numpy functions np.mean() and np.std() to compute the mean and standard deviations.
'''

# Import scale
from sklearn.preprocessing import scale

# Scale the features: X_scaled
X_scaled = scale(X)

# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(np.mean(X))) 
print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(np.mean(X_scaled))) 
print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))
