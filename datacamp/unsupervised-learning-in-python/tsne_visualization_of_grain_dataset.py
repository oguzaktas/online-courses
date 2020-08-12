'''
Instructions
- Import TSNE from sklearn.manifold.
- Create a TSNE instance called model with learning_rate=200.
- Apply the .fit_transform() method of model to samples. Assign the result to tsne_features.
- Select the column 0 of tsne_features. Assign the result to xs.
- Select the column 1 of tsne_features. Assign the result to ys.
- Make a scatter plot of the t-SNE features xs and ys. To color the points by the grain variety, specify the additional keyword argument c=variety_numbers.
'''

# Import TSNE and matplotlib
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Create a TSNE instance: model
model = TSNE(learning_rate=200)

# Apply fit_transform to samples: tsne_features
tsne_features = model.fit_transform(samples)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1st feature: ys
ys = tsne_features[:,1]

# Scatter plot, coloring by variety_numbers
plt.scatter(xs, ys, c=variety_numbers)
plt.show()
