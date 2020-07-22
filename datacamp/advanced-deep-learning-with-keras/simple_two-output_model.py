'''
Instructions
- Create a single input layer with 2 columns.
- Connect this input to a Dense layer with 2 units.
- Create a model with input_tensor as the input and output_tensor as the output.
- Compile the model with 'adam' as the optimizer and 'mean_absolute_error' as the loss function.
'''

# Define the input
input_tensor = Input(shape=(2,))

# Define the output
output_tensor = Dense(2)(input_tensor)

# Create a model
model = Model(input_tensor, output_tensor)

# Compile the model
model.compile(optimizer='adam', loss='mean_absolute_error')