'''
Instructions
- Import the constant submodule from the tensorflow module.
- Convert the credit_numpy array into a constant object in tensorflow. Do not set the data type.
'''

# Import constant from TensorFlow
from tensorflow import constant

# Convert the credit_numpy array into a tensorflow constant
credit_constant = constant(credit_numpy)

# Print constant datatype
print('The datatype is:', credit_constant.dtype)

# Print constant shape
print('The shape is:', credit_constant.shape)
