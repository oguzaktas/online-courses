'''
Instructions
- Compute products1 by matrix multiplying the features tensor by the weights.
- Use a sigmoid activation function to transform products1 + bias1.
- Print the shapes of borrower_features, weights1, bias1, and dense1.
'''

# Compute the product of borrower_features and weights1
products1 = matmul(borrower_features, weights1)

# Apply a sigmoid activation function to products1 + bias1
dense1 = keras.activations.sigmoid(products1 + bias1)

# Print the shapes of borrower_features, weights1, bias1, and dense1
print('\n shape of borrower_features: ', borrower_features.shape)
print('\n shape of weights1: ', weights1.shape)
print('\n shape of bias1: ', bias1.shape)
print('\n shape of dense1: ', dense1.shape)

'''
Output:
<script.py> output:
    
     shape of borrower_features:  (5, 3)
    
     shape of weights1:  (3, 2)
    
     shape of bias1:  (1,)
    
     shape of dense1:  (5, 2)
'''