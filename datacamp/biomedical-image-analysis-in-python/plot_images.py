'''
Instructions
- Set the stage by importing packages and loading the CT scan. matplotlib.pyplot is often loaded as plt.
- Draw the image with plt.imshow(), selecting the "gray" colormap. Call plt.show() to render the image.
- Draw the image in grayscale. Also, set vmin=-200 and vmax=200 to increase the contrast 
(i.e., the distance between the brightest and darkest colors is smaller than before).
- Turn axis ticks and labels off.
'''

# Import ImageIO and PyPlot 
import imageio
import matplotlib.pyplot as plt

# Read in "chest-220.dcm"
im = imageio.imread('chest-220.dcm')

# Draw the image in grayscale
plt.imshow(im, cmap="gray")

# Render the image
plt.show()

# Draw the image with greater contrast
plt.imshow(im, vmin=-200, vmax=200)

# Render the image
plt.show()

# Remove axis ticks and labels
plt.axis('off')

# Render the image
plt.show()
