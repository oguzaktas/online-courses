'''
Instructions
- Import the data and the module needed for contouring detection.
- Obtain the horse image shown in the context area.
- Find the contours of the horse image using a constant level value of 0.8.
'''

# Import the modules
from skimage import measure, data

# Obtain the horse image
horse_image = data.horse()

# Find the contours with a constant level value of 0.8
contours = measure.find_contours(horse_image, 0.8)

# Shows the image with contours found
show_image_contour(horse_image, contours)
