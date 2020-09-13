'''
Instructions
- Import the module.
- Obtain the binarized and dilated image, from the original image world_image.
'''

# Import the module
from skimage import morphology

# Obtain the dilated image 
dilated_image = morphology.binary_dilation(world_image)

# See results
show_image(world_image, 'Original')
show_image(dilated_image, 'Dilated image')
