'''
Instructions
- Obtain a reference to the outputs of the first convolutional layer in the model.
- Build a new model using the model's input and the layer_output as outputs.
- Use this first_layer_model to predict on X_test.
- Plot the activations of the first digit of X_test for the 15th and the 18th neuron filter.
'''

# Obtain a reference to the outputs of the first layer
layer_output = model.layers[0].output

# Build a model using the model's input and the first layer output
first_layer_model = Model(inputs = model.input, outputs = layer_output)

# Use this model to predict on X_test
activations = first_layer_model.predict(X_test)

# Plot the activations of first digit of X_test for the 15th filter
axs[0].matshow(activations[0,:,:,14], cmap = 'viridis')

# Do the same but for the 18th filter now
axs[1].matshow(activations[0,:,:,18], cmap = 'viridis')
plt.show()