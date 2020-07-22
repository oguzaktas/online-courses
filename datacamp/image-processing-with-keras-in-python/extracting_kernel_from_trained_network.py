'''
Instructions
- Load the weights into the model from the file weights.hdf5.
- Get the first convolutional layer in the model from the layers attribute.
- Use the .get_weights() method to extract the weights from this layer.
'''

# Load the weights into the model
model.load_weights('weights.hdf5')

# Get the first convolutional layer from the model
c1 = model.layers[0]

# Get the weights of the first convolutional layer
weights1 = c1.get_weights()

# Pull out the first channel of the first kernel in the first layer
kernel = weights1[0][...,0, 0]
print(kernel)
