'''
Instructions
- Import imageio.
- Read in the image "chest-220.dcm" using the imread() function.
- Print the type() and shape (number of pixels) of im.
'''

# Import ImageIO
import imageio

# Load "chest-220.dcm"
im = imageio.imread('chest-220.dcm')

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)
