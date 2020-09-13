'''
Instructions
- Transform the image to grayscale using rgb2gray().
- Obtain the optimal threshold value for the image and set it as thresh.
- Apply thresholding to the image once you have the optimal threshold value thresh, using the corresponding operator.
- Apply the corresponding function to obtain the contours and use a value level of 0.8.
'''

# color, measure and filters modules are already imported so you can use the functions to find contours and apply thresholding.

# Make the image grayscale
image_dices = color.rgb2gray(image_dices)

# Obtain the optimal thresh value
thresh = threshold_otsu(image_dices)

# Apply thresholding
binary = image_dices > thresh

# Find contours at a constant value of 0.8
contours = measure.find_contours(binary, 0.8)

# Show the image
show_image_contour(image_dices, contours)
