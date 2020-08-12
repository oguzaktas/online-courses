'''
Instructions
- Create a single input layer with 2 columns.
- The first output layer should have 1 unit with 'linear' activation and no bias term.
- The second output layer should have 1 unit with 'sigmoid' activation and no bias term. Also, use the first output layer as an input to this layer.
- Create a model with these input and outputs.
'''

# Create an input layer with 2 columns
input_tensor = Input(shape=(2,))

# Create the first output
output_tensor_1 = Dense(1, activation='linear', use_bias=False)(input_tensor)

# Create the second output (use the first output as input here)
output_tensor_2 = Dense(1, activation='sigmoid', use_bias=False)(output_tensor_1)

# Create a model with 2 outputs
model = Model(input_tensor, [output_tensor_1, output_tensor_2])