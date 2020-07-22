'''
Instructions
- Import the module and the rotating and rescaling functions.
- Rotate the image 90 degrees clockwise.
- Rescale the cat_image to be 4 times smaller and apply the anti aliasing filter. Set whether or not the image should be treated as multichannel (colored).
- Rescale the rotated_cat_image to be 4 times smaller without applying an anti aliasing filter.
'''

# Import the module and the rotate and rescale functions
from skimage.transform import rotate, rescale

# Rotate the image 90 degrees clockwise 
rotated_cat_image = rotate(image_cat, -90)

# Rescale with anti aliasing
rescaled_with_aa = rescale(rotated_cat_image, 1/4, anti_aliasing=True, multichannel=True)

# Rescale without anti aliasing
rescaled_without_aa = rescale(rotated_cat_image, 1/4, anti_aliasing=False, multichannel=True)

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")
