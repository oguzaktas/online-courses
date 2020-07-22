'''
Instructions
- Find the words corresponding to the 5 largest coefficients.
- Find the words corresponding to the 5 smallest coefficients.
'''

import numpy as np

# Get the indices of the sorted cofficients
inds_ascending = np.argsort(lr.coef_.flatten()) 
inds_descending = inds_ascending[::-1]

# Print the most positive words
print("Most positive words: ", end="")
for i in range(5):
    print(vocab[inds_descending[4]], end=", ")
print("\n")

# Print most negative words
print("Most negative words: ", end="")
for i in range(5):
    print(vocab[inds_ascending[4]], end=", ")
print("\n")
