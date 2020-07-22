'''
Instructions
- Import TSNE from sklearn.manifold.
- Create a TSNE instance called model with learning_rate=50.
- Apply the .fit_transform() method of model to normalized_movements. Assign the result to tsne_features.
- Select column 0 and column 1 of tsne_features.
- Make a scatter plot of the t-SNE features xs and ys. Specify the additional keyword argument alpha=0.5.
- Code to label each point with its company name has been written for you using plt.annotate(), so just hit 'Submit Answer' to see the visualization!
'''

# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=50)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1th feature: ys
ys = tsne_features[:,1]

# Scatter plot
plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()
