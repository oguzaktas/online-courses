'''
Instructions
- Find the center-point of im using ndi.center_of_mass().
- Calculate the distance from the image center (128, 128), along each axis.
- Use ndi.shift() to shift the data.
- Plot the original and shifted data. First, create an array of subplots with two rows 
and one column. Then, draw im and xfm on the first and second subplots.
'''

import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

# Find image center of mass
com = ndi.center_of_mass(im)

# Calculate amount of shift needed
d0 = 128 - com[0]
d1 = 128 - com[1]

# Translate the brain towards the center
xfm = ndi.shift(im, shift=[d0, d1])

# Find image center of mass
com = ndi.center_of_mass(im)

# Calculate amount of shift needed
d0 = 128 - com[0]
d1 = 128 - com[1]

# Translate the brain towards the center
xfm = ndi.shift(im, shift=(d0, d1))

# Plot the original and adjusted images
fig, axes = plt.subplots(2, 1)
axes[0].imshow(im)
axes[1].imshow(xfm)
format_and_render_plot()
