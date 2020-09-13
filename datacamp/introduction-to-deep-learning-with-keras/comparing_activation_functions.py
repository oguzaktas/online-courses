'''
Instructions
- Fill up the activation functions array with relu,leaky_relu, sigmoid, and tanh.
- Get a new model for each iteration with get_model() passing the current activation function as a parameter.
- Fit your model providing the train and validation_data, use 20 epochs and set verbose to 0.
'''

# Activation functions to try
activations = ['relu', 'leaky_relu', 'sigmoid', 'tanh']

# Loop over the activation functions
activation_results = {}

for act in activations:
  # Get a new model with the current activation
  model = get_model(act)
  # Fit the model
  history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, verbose=0)
  activation_results[act] = history
