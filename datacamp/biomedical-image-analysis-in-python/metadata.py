'''
Instructions
- Read in the image, "chest-220.dcm".
- Print the available keys in the metadata dictionary. Use the the keys() method of im.meta.
'''

# Import ImageIO and load image
import imageio
im = imageio.imread('chest-220.dcm')

# Print the available metadata fields
print(im.meta.keys())

# Print the available metadata items
print(im.meta.items())