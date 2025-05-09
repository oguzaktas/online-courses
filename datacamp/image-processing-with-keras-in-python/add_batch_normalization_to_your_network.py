'''
Instructions
- Add the first convolutional layer. You can use the img_rows and img_cols objects available in your workspace to define the input_shape of this layer.
- Add batch normalization applied to the outputs of the first layer.
'''

# Add a convolutional layer
model.add(Conv2D(15, kernel_size=2, activation='relu', input_shape=(img_rows, img_cols, 1)))

# Add batch normalization layer
model.add(BatchNormalization())

# Add another convolutional layer
model.add(Conv2D(5, kernel_size=2, activation='relu'))

# Flatten and feed to output layer
model.add(Flatten())
model.add(Dense(3, activation='softmax'))
