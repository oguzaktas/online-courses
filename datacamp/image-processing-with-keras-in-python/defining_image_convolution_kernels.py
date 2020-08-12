'''
Instructions
- Define a kernel that finds horizontal lines in images.
- Define a kernel that finds a light spot surrounded by dark pixels.
- Define a kernel that finds a dark spot surrounded by bright pixels.
'''

import numpy as np

# kernel that finds horizontal lines in images.
kernel = np.array([[-1, -1, -1], 
                   [1, 1, 1],
                   [-1, -1, -1]])

# kernel that finds a light spot surrounded by dark pixels.
kernel = np.array([[-1, -1, -1], 
                   [-1, 1, -1],
                   [-1, -1, -1]])

kernel = np.array([[1, 1, 1], 
                   [1, -1, 1],
                   [1, 1, 1]])
