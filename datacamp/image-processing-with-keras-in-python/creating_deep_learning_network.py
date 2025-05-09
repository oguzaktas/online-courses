'''
Instructions
- The first convolutional layer is the input layer of the network. This should have 15 units with kernels of 2 by 2 pixels. 
It should have a 'relu' activation function. It can use the variables img_rows and img_cols to define its input_shape.
- The second convolutional layer receives its inputs from the first layer. It should have 
5 units with kernels of 2 by 2 pixels. It should also have a 'relu' activation function.
'''

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

model = Sequential()

# Add a convolutional layer (15 units)
model.add(Conv2D(15, kernel_size=2, activation='relu', input_shape=(img_rows, img_cols, 1)))


# Add another convolutional layer (5 units)
model.add(Conv2D(5, kernel_size=2, activation='relu'))

# Flatten and feed to output layer
model.add(Flatten())
model.add(Dense(3, activation='softmax'))
