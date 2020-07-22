'''
# a simple dense layer
import tensorflow as tf
inputs = tf.constant([[1, 35]])
weights = tf.Variable([[-0.05], [-0.01]])
bias = tf.Variable([0.5])
product = tf.matmul(inputs, weights)
dense = tf.keras.activations.sigmoid(product + bias)
# defining first dense layer
dense1 = tf.keras.layers.Dense(10, activation='sigmoid')(inputs)
dense2 = tf.keras.layers.Dense(5, activation='sigmoid')(dense1)
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(dense2)
'''

'''
Instructions
- Initialize weights1 as a variable using a 3x2 tensor of ones.
- Compute the product of borrower_features by weights1 using matrix multiplication.
- Use a sigmoid activation function to transform product1 + bias1.
- Initialize weights2 as a variable using a 2x1 tensor of ones.
- Compute the product of dense1 by weights2 using matrix multiplication.
- Use a sigmoid activation function to transform product2 + bias2.
'''

# Initialize bias1
bias1 = Variable(1.0)

# Initialize weights1 as 3x2 variable of ones
weights1 = Variable(ones((3, 2)))

# Perform matrix multiplication of borrower_features and weights1
product1 = matmul(borrower_features, weights1)

# Apply sigmoid activation function to product1 + bias1
dense1 = keras.activations.sigmoid(product1 + bias1)

# Print shape of dense1
print("\n dense1's output shape: {}".format(dense1.shape))

# Initialize bias2 and weights2
bias2 = Variable(1.0)
weights2 = Variable(ones((2, 1)))

# Perform matrix multiplication of dense1 and weights2
product2 = matmul(dense1, weights2)

# Apply activation to product2 + bias2 and print the prediction
prediction = keras.activations.sigmoid(product2 + bias2)
print('\n prediction: {}'.format(prediction.numpy()[0,0]))
print('\n actual: 1')

'''
Output:
 prediction: 0.9525741338729858
 actual: 1
'''