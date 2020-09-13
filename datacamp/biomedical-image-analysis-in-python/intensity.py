'''
Instructions
- Load the image "hand-xray.jpg" using imageio.
- Print the image's data type (dtype), minimum (min()) and maximum intensity (max()).
- Plot the image using plt.imshow(). Explicitly set the colormap's minimum (0) and maximum (255) values using the vmin and vmax arguments.
- Add a colorbar using plt.colorbar(), then render the plot using the custom function format_and_render_plot(). This has been done for you.
'''

import imageio
import numpy as np
import matplotlib.pyplot as plt

# Load the hand radiograph
im = imageio.imread('hand-xray.jpg')
print('Data type:', im.dtype)
print('Min. value:', im.min())
print('Max value:', im.max())

# Plot the grayscale image
plt.imshow(im, vmin=0, vmax=255)
plt.colorbar()
format_and_render_plot()
