'''
Instructions
- Import the required module.
- Show the histogram from the original x-ray image chest_xray_image, using the hist() function.
- Use histogram equalization on chest_xray_image to obtain the improved image and load it as xray_image_eq.
- Show the resulting improved image xray_image_eq.
'''

# Import the required module
from skimage import exposure

import matplotlib.pyplot as plt

# Show original x-ray image and its histogram
show_image(chest_xray_image, 'Original x-ray')

plt.title('Histogram of image')
plt.hist(chest_xray_image.ravel(), bins=256)
plt.show()

# Use histogram equalization to improve the contrast
xray_image_eq =  exposure.equalize_hist(chest_xray_image)

# Show the resulting image
show_image(xray_image_eq, 'Resulting image')
