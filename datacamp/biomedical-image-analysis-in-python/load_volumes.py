'''
Instructions
- Use volread() to load the directory, "tcia-chest-ct".
- Print the available metadata using the keys() method of vol.meta.
- Print the shape of the volume.
'''

# Import ImageIO
import imageio

# Load the "tcia-chest-ct" directory
vol = imageio.volread('tcia-chest-ct')

# Print image attributes
print('Available metadata:', vol.meta.keys())
print('Shape of image array:', vol.shape)
