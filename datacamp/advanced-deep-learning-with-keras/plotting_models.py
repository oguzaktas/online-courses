'''
Instructions
- Save the model plot to the file 'model.png'.
- Import and display 'model.png' into Python using matplotlib.
'''

# Imports
import matplotlib.pyplot as plt
from keras.utils import plot_model

# Plot the model
plot_model(model, to_file='model.png')

# Display the image
data = plt.imread('model.png')
plt.imshow(data)
plt.show()