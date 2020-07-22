'''
Instructions
- Create a bone mask by selecting pixels with intensities greater than or equal to 145.
- Create a skin mask by selecting pixels with intensities greater than or equal to 45 and less than 145.
- Plot the skin and bone masks in grayscale.
'''

import matplotlib.pyplot as plt

# Create skin and bone masks
mask_bone = im >= 145
mask_skin = (im >= 45) & (im < 145)

# Plot the skin (0) and bone (1) masks
fig, axes = plt.subplots(1,2)
axes[0].imshow(mask_skin, cmap='gray')
axes[1].imshow(mask_bone, cmap='gray')
format_and_render_plot()
