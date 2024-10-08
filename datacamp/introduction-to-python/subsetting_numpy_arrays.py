'''
Instructions
- Subset np_weight: print out the element at index 50.
- Print out a sub-array of np_height: It contains the elements at index 100 up to and including index 110
'''
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])
