'''
Instructions
- Import the module that includes the Contrast Limited Adaptive Histogram Equalization (CLAHE) function.
- Obtain the image you'll work on, with a cup of coffee in it, from the module that holds all the images for testing purposes.
- From the previously imported module, call the function to apply the adaptive 
equalization method on the original image and set the clip limit to 0.03.
'''

# Import the necessary modules
from skimage import data, exposure

# Load the image
original_image = data.coffee()

# Apply the adaptive equalization on the original image
adapthist_eq_image = exposure.equalize_adapthist(original_image, clip_limit=0.03)

# Compare the original image to the equalized
show_image(original_image)
show_image(adapthist_eq_image, '#ImageProcessingDatacamp')
