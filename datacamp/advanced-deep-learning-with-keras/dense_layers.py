'''
Instructions
- Import the Dense layer function from keras.layers.
- Create a Dense layer with 1 unit.
- Pass input_tensor to output_layer().
'''

# Load layers
from keras.layers import Input, Dense

# Input layer
input_tensor = Input(shape=(1,))

# Dense layer
output_layer = Dense(1)

# Connect the dense layer to the input_tensor
output_tensor = output_layer(input_tensor)