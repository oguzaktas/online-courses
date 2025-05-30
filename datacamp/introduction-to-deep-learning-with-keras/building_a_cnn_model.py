'''
Instructions
- Import the Conv2D and Flatten layers and instantiate your model.
- Add a first convolutional layer with 32 filters of size 3x3 and the corresponding 3D tuple as input_shape.
- Add a second convolutional layer with 16 filters of size 3x3 with relu activation.
- Flatten the previous layer output to create a one-dimensional vector.
'''

# Import the Conv2D and Flatten layers and instantiate model
from keras.layers import Conv2D, Flatten
model = Sequential()

# Add a convolutional layer of 32 filters of size 3x3
model.add(Conv2D(32, input_shape=(28, 28, 1), kernel_size=3, activation='relu'))

# Add a convolutional layer of 16 filters of size 3x3
model.add(Conv2D(16, kernel_size=3, activation='relu'))

# Flatten the previous layer output
model.add(Flatten())

# Add as many outputs as classes with softmax activation
model.add(Dense(10, activation='softmax'))