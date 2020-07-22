'''
Instructions
- Import the canny edge detector from the feature module.
- Convert the image to grayscale, using the method from the color module used in previous chapters.
- Apply the canny edge detector to the grapefruit image.
'''

# Import the canny edge detector 
from skimage.feature import canny

# Convert image to grayscale
grapefruit = color.rgb2gray(grapefruit)

# Apply canny edge detector
canny_edges = canny(grapefruit)

# Show resulting image
show_image(canny_edges, "Edges with Canny")
