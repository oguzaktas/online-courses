'''
Instructions
- Import the required module from scikit-image.
- Use the histogram equalization function from the module previously imported.
- Show the resulting image.
'''

# Import the required module
from skimage import exposure

# Use histogram equalization to improve the contrast
image_eq =  exposure.equalize_hist(image_aerial)

# Show the original and resulting image
show_image(image_aerial, 'Original')
show_image(image_eq, 'Resulting image')
