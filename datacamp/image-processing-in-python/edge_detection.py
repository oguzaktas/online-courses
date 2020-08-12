'''
Instructions
- Import the color module so you can convert the image to grayscale.
- Import the filters module and sobel() function.
- Make soaps_image grayscale using the appropriate method from the color module.
- Apply the sobel edge detection filter on the obtained grayscale image soaps_image_gray.
'''

# Import the color module
from skimage import color

# Import the filters module and sobel function
from skimage.filters import sobel

# Make the image grayscale
soaps_image_gray = color.rgb2gray(soaps_image)

# Apply edge detection filter
edge_sobel = sobel(soaps_image_gray)

# Show original and resulting image to compare
show_image(soaps_image, "Original")
show_image(edge_sobel, "Edges with Sobel")
