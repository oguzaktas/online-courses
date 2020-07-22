'''
Instructions
- Import:
    - linkage and dendrogram from scipy.cluster.hierarchy.
    - matplotlib.pyplot as plt.
- Perform hierarchical clustering on samples using the linkage() function with the method='single' keyword argument. Assign the result to mergings.
- Plot a dendrogram of the hierarchical clustering, using the list country_names as the labels. In addition, specify the leaf_rotation=90, 
and leaf_font_size=6 keyword arguments as you have done earlier.
'''

# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Calculate the linkage: mergings
mergings = linkage(samples, method='single')

# Plot the dendrogram
dendrogram(mergings, labels=country_names, leaf_rotation=90, leaf_font_size=6)
plt.show()
