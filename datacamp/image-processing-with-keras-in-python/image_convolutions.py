'''
Instructions
- Select the right window from the image in each iteration and multiply this part of the image with the kernel.
- Sum the result and allocate the sum to the correct entry in the output array (results).
'''

import numpy as np

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
result = np.zeros(im.shape)

# Output array
for ii in range(im.shape[0] - 3):
    for jj in range(im.shape[1] - 3):
        result[ii, jj] = (im[ii:ii+3, jj:jj+3] * kernel).sum()

# Print result
print(result)
