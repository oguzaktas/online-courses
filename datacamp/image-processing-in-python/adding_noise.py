'''
Instructions
- Import the util module and the random noise function.
- Add noise to the image.
- Show the original and resulting image.
'''

# Import the module and function
from skimage.util import random_noise

# Add noise to the image
noisy_image = random_noise(fruit_image)

# Show original and resulting image
show_image(fruit_image, 'Original')
show_image(noisy_image, 'Noisy image')
