'''
Instructions
- In the first dense layer, set the number of nodes to 16, the activation to sigmoid, and the input_shape to (784,).
- Apply dropout at a rate of 25% to the first layer's output.
- Set the output layer to be dense, have 4 nodes, and use a softmax activation function.
- Compile the model using an adam optimizer and categorical_crossentropy loss function.
'''

# Define the first dense layer
model.add(keras.layers.Dense(16, activation='sigmoid', input_shape=(784,)))

# Apply dropout to the first layer's output
model.add(keras.layers.Dropout(0.25))

# Define the output layer
model.add(keras.layers.Dense(4, activation='softmax'))

# Compile the model
model.compile('adam', loss='categorical_crossentropy')

# Print a model summary
print(model.summary())

'''
Output:
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 16)                12560     
_________________________________________________________________
dropout (Dropout)            (None, 16)                0         
_________________________________________________________________
dense_1 (Dense)              (None, 4)                 68        
=================================================================
Total params: 12,628
Trainable params: 12,628
Non-trainable params: 0
_________________________________________________________________
None
'''