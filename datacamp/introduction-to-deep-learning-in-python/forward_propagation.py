# forward propagation

'''
The input data has been pre-loaded as input_data, and the weights are available in a dictionary called weights. 
The array of weights for the first node in the hidden layer are in weights['node_0'], 
and the array of weights for the second node in the hidden layer are in weights['node_1'].

The weights feeding into the output node are available in weights['output'].
'''

import numpy as np

input_data = np.array([2, 3])

weights = {'node_0': np.array([1, 1]), 
'node_1': np.array([-1, 1]),
'output': np.array([2, -1])}

node_0_value = (input_data * weights['node_0']).sum()
node_1_value = (input_data * weights['node_1']).sum()

hidden_layer_values = np.array([node_0_value, node_1_value])
print(hidden_layer_values)

output = (hidden_layer_values * weights['output']).sum()
print(output)
