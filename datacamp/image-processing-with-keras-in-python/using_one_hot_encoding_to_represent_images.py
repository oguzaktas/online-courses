'''
Instructions
- Initialize the ohe_labels variable to hold the one-hot encoded array.
- Use np.where() to find the location of the category of the item in each iteration in categories.
- Assign a 1 into the correct row/column combination in every iteration.
'''

import numpy as np

# The number of image categories
n_categories = 3

# The unique values of categories in the data
categories = np.array(["shirt", "dress", "shoe"])

# Initialize ohe_labels as all zeros
ohe_labels = np.zeros((len(labels), n_categories))

# Loop over the labels
for ii in range(len(labels)):
    # Find the location of this label in the categories variable
    jj = np.where(categories == labels[ii])
    # Set the corresponding zero to one
    ohe_labels[ii, jj] = 1
