'''
Instructions
- Import imageio and numpy (as np).
- Load "chest-220.dcm", "chest-221.dcm", and "chest-222.dcm".
- Create a 3D volume using np.stack(). Set the stacking axis to 0.
- Print the shape attribute of vol.
'''

# Import ImageIO and NumPy
import imageio
import numpy as np

# Read in each 2D image
im1 = imageio.imread('chest-220.dcm')
im2 = imageio.imread('chest-221.dcm')
im3 = imageio.imread('chest-222.dcm')

# Stack images into a volume
vol = np.stack(np.stack([im1, im2, im3]))
print('Volume dimensions:', vol.shape)
