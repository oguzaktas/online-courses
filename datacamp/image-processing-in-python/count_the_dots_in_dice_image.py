'''
Instructions
- Make shape_contours be a list with all contour shapes of contours.
- Set max_dots_shape to 50.
- Set the shape condition of the contours to be the maximum shape size of the dots max_dots_shape.
- Print the dice's number.
'''

# Create list with the shape of each contour
shape_contours = [cnt.shape[0] for cnt in contours]

# Set 50 as the maximum size of the dots shape
max_dots_shape = 50

# Count dots in contours excluding bigger than dots size
dots_contours = [cnt for cnt in contours if np.shape(cnt)[0] < max_dots_shape]

# Shows all contours found 
show_image_contour(binary, contours)

# Print the dice's number
print("Dice's dots number: {}. ".format(len(dots_contours)))
