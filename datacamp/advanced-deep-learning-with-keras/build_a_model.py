'''
Instructions
- Import Model from keras.models to create a keras model.
- Use the input layer and output layer you already defined as the model's input and output.
'''

# Input/dense/output layers
from keras.layers import Input, Dense
input_tensor = Input(shape=(1,))
output_tensor = Dense(1)(input_tensor)

# Build the model
from keras.models import Model
model = Model(input_tensor, output_tensor)