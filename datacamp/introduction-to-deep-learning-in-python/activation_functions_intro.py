# activation functions intro

'''
An "activation function" is a function applied at each node. It converts the node's input into some output.

The input data has been pre-loaded as input_data, and the weights are available in a dictionary called weights. 
The array of weights for the first node in the hidden layer are in weights['node_0'], 
and the array of weights for the second node in the hidden layer are in weights['node_1'].

The weights feeding into the output node are available in weights['output'].
'''

import numpy as np

input_data = np.array([-1, 2])

weights = {'node_0': np.array([3, 3]), 
'node_1': np.array([1, 5]),
'output': np.array([2, -1])}

node_0_input = (input_data * weights['node_0']).sum()
node_0_output = np.tanh(node_0_input)

node_1_input = (input_data * weights['node_1']).sum()
node_1_output = np.tanh(node_1_input)

hidden_layer_values = np.array([node_0_output, node_1_output])
print(hidden_layer_values)

output = (hidden_layer_values * weights['output']).sum()
print(output)
