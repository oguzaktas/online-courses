'''
Instructions
- Apply a median filter to im. Set the size to 3.
- Create a mask of values greater than 60, then use ndi.binary_closing() to fill small holes in it.
- Extract a labeled array and the number of labels using ndi.label().
- Plot the labels array on top of the original image. To create an overlay, use np.where to convert values of 0 to np.nan. 
Then, plot the overlay with the rainbow colormap and set alpha=0.75 to make it transparent.
'''

import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

# Smooth intensity values
im_filt = ndi.median_filter(im, size=3)

# Select high-intensity pixels
mask_start = np.where(im_filt > 60, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)

# Create a `labels` overlay
overlay = np.where(labels > 0, labels, np.nan)

# Use imshow to plot the overlay
plt.imshow(overlay, cmap='rainbow', alpha=0.75)
format_and_render_plot()
