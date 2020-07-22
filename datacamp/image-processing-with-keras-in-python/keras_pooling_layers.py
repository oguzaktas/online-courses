'''
Instructions
- Add an input convolutional layer (15 units, kernel size of 2, relu activation).
- Add a maximum pooling operation (pooling over windows of size 2x2).
- Add another convolution layer (5 units, kernel size of 2, relu activation).
- Flatten the output of the second convolution and add a Dense layer for output (3 categories, softmax activation).
'''

# Add a convolutional layer
model.add(Conv2D(15, kernel_size=2, activation='relu', 
                 input_shape=(img_rows, img_cols, 1)))

# Add a pooling operation
model.add(MaxPool2D(2))

# Add another convolutional layer
model.add(Conv2D(5, kernel_size=2, activation='relu'))

# Flatten and feed to output layer
model.add(Flatten())
model.add(Dense(3, activation='softmax'))
model.summary()
