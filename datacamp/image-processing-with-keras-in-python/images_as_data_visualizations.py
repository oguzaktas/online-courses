'''
Instructions
- Import the image from the file bricks.png into data.
- Display the image in data on the screen.
'''

# Import matplotlib
import matplotlib.pyplot as plt

# Load the image
data = plt.imread('bricks.png')

# Display the image
plt.imshow(data)
plt.show()
