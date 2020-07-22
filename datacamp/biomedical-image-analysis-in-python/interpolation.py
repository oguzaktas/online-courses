'''
Instructions
- Use ndi.zoom() to upsample im from a shape of 128, 128 to 512, 512 twice. First, use an interpolation order of 0, then set order to 5.
- Print the array shapes of im and up0.
- Plot close-ups of the images. Use the index range 128:256 along each axis.
'''

import matplotlib.pyplot as plt

# Upsample "im" by a factor of 4
up0 = ndi.zoom(im, zoom=4, order=0)
up5 = ndi.zoom(im, zoom=4, order=5)

# Print original and new shape
print('Original shape:', im.shape)
print('Upsampled shape:', up5.shape)

# Plot close-ups of the new images
fig, axes = plt.subplots(1, 2)
axes[0].imshow(up0[128:256, 128:256])
axes[1].imshow(up5[128:256, 128:256])
format_and_render_plots()
