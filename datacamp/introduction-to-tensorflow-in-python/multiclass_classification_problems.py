'''
Instructions
- Define the input layer as a 32-bit constant tensor using borrower_features.
- Set the first dense layer to have 10 output nodes and a sigmoid activation function.
- Set the second dense layer to have 8 output nodes and a rectified linear unit activation function.
- Set the output layer to have 6 output nodes and the appropriate activation function.
'''

# Construct input layer from borrower features
inputs = constant(borrower_features, float32)

# Define first dense layer
dense1 = keras.layers.Dense(10, activation='sigmoid')(inputs)

# Define second dense layer
dense2 = keras.layers.Dense(8, activation='relu')(dense1)

# Define output layer
outputs = keras.layers.Dense(6, activation='softmax')(dense2)

# Print first five predictions
print(outputs.numpy()[:5])

'''
Output:
[[0.20871335 0.16661178 0.20108487 0.1750592  0.12725635 0.12127451]
 [0.12187891 0.16740733 0.06671306 0.20511945 0.24677028 0.19211106]
 [0.11027827 0.20583428 0.09551102 0.23281796 0.21278518 0.14277332]
 [0.17693152 0.1613864  0.05985694 0.26463667 0.2340488  0.10313965]
 [0.30505964 0.11743025 0.17319965 0.15247901 0.11269657 0.13913494]]
'''