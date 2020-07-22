'''
Instructions
- Import the Input and Dense functions from keras.layers.
- Create an input layer of shape 1.
- Again, create a dense layer with 1 unit and pass input_tensor directly to it.
'''

# Load layers
from keras.layers import Input, Dense

# Input layer
input_tensor = Input(shape=(1,))

# Create a dense layer and connect the dense layer to the input_tensor in one step
# Note that we did this in 2 steps in the previous exercise, but are doing it in one step now
output_tensor = Dense(1)(input_tensor)