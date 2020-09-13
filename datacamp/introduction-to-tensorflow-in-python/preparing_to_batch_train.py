'''
# Minimize the loss function
opt.minimize(lambda: loss_function(intercept, slope, price_batch, size_batch), var_list=[intercept, slope])
# Print parameter values
print(intercept.numpy(), slope.numpy())
'''

'''
Instructions
- Define intercept as having an initial value of 10.0 and a data type of 32-bit float.
- Define the model to return the predicted values using intercept, slope, and features.
- Define a function called loss_function() that takes intercept, slope, targets, and features as arguments and in that order. Do not set default argument values.
- Define the mean squared error loss function using targets and predictions.
'''

# Define the intercept and slope
intercept = Variable(10.0, float32)
slope = Variable(0.5, float32)

# Define the model
def linear_regression(intercept, slope, features):
	# Define the predicted values
	return intercept + slope * features

# Define the loss function
def loss_function(intercept, slope, targets, features):
	# Define the predicted values
	predictions = linear_regression(intercept, slope, features)
    
 	# Define the MSE loss
	return keras.losses.mse(targets, predictions)
