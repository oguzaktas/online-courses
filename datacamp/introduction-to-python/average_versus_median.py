'''
Instructions
- Create numpy array np_height that is equal to first column of np_baseball.
- Print out the mean of np_height.
- Print out the median of np_height.
'''
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height = np.array(np_baseball[:,0])

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))
