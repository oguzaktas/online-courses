'''
Instructions
- Shift im 20 pixels left and 20 pixels up, i.e. (-20, -20). Then, rotate it 35 degrees downward. Remember to specify a value for reshape.
- Use ndi.zoom() to downsample the image from (256, 256) to (64, 64).
- Use ndi.zoom() to upsample the image from (256, 256) to (1024, 1024).
- Plot the resampled images.
'''

import matplotlib.pyplot as plt

# Center and level image
xfm = ndi.shift(im, shift=(-20, -20))
xfm = ndi.rotate(xfm, angle=-35, reshape=False)

# Resample image
im_dn = ndi.zoom(xfm, zoom=0.25)
im_up = ndi.zoom(xfm, zoom=4.00)

# Plot the images
fig, axes = plt.subplots(2, 1)
axes[0].imshow(im_dn)
axes[1].imshow(im_up)
format_and_render_plot()
