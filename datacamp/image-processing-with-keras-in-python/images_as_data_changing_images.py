'''
Instructions
- Modify the bricks image to replace the top left corner of the image (10 by 10 pixels) into a red square.
- Visualize the resulting image.
'''

import matplotlib.pyplot as plt

# Set the red channel in this part of the image to 1
data[:10, :10, 0] = 1

# Set the green channel in this part of the image to 0
data[:10, :10, 1] = 0

# Set the blue channel in this part of the image to 0
data[:10, :10, 2] = 0

# Visualize the result
plt.imshow(data)
plt.show()
