'''
Information: Unlike NMF, PCA doesn't learn the parts of things. Its components do not correspond to topics 
(in the case of documents) or to parts of images, when trained on images.

Instructions
- Import PCA from sklearn.decomposition.
- Create a PCA instance called model with 7 components.
- Apply the .fit_transform() method of model to samples. Assign the result to features.
- To each component of the model (accessed via model.components_), apply the show_as_image() function to that component inside the loop.
'''

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
