'''
Instructions
- Apply the canny edge detector to the grapefruit image with a sigma of 1.8.
- Apply the canny edge detector to the grapefruit image with a sigma of 2.2.
- Show the resulting images.
'''

from skimage.feature import canny

# Apply canny edge detector with a sigma of 1.8
edges_1_8 = canny(grapefruit, sigma=1.8)

# Apply canny edge detector with a sigma of 2.2
edges_2_2 = canny(grapefruit, sigma=2.2)

# Show resulting images
show_image(edges_1_8, "Sigma of 1.8")
show_image(edges_2_2, "Sigma of 2.2")
