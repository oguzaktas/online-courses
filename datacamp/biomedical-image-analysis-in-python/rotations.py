'''
Instructions
- Shift im towards the center: 20 pixels left and 20 pixels up.
- Use ndi.rotate to turn xfm 30 degrees downward. Set reshape=False to prevent the image shape from changing.
- Plot the original and transformed images.
'''

import matplotlib.pyplot as plt

# Shift the image towards the center
xfm = ndi.shift(im, shift=(-20, -20))

# Rotate the shifted image
xfm = ndi.rotate(xfm, angle=-30, reshape=False)

# Plot the original and transformed images
fig, axes = plt.subplots(2, 1)
axes[0].imshow(im)
axes[1].imshow(xfm)
format_and_render_plot()
