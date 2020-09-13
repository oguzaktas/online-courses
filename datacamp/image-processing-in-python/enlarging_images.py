'''
Instructions
- Import the module and function needed to enlarge images, you'll do this by rescaling.
- Import the data module.
- Load the rocket() image from data.
- Enlarge the rocket_image so it is 4 times bigger, with the anti aliasing filter applied. Make sure to set multichannel to True or you risk your session timing out!
'''

# Import the module and function to enlarge images
from skimage.transform import rescale

# Import the data module
from skimage import data

# Load the image from data
rocket_image = data.rocket()

# Enlarge the image so it is 4 times bigger
enlarged_rocket_image = rescale(rocket_image, 4, anti_aliasing=True, multichannel=True)

# Show original and resulting image
show_image(rocket_image)
show_image(enlarged_rocket_image, "4 times enlarged image")
