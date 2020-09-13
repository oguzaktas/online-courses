'''
Instructions
- Use the convolution() function to convolve the extracted kernel with the first channel of the fourth item in the image array.
- Visualize the resulting convolution with imshow().
'''

import matplotlib.pyplot as plt

# Convolve with the fourth image in test_data
out = convolution(test_data[3, :, :, 0], kernel)

# Visualize the result
plt.imshow(out)
plt.show()
