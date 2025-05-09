'''
Instructions
- Set opt to use the stochastic gradient descent optimizer (SGD) with a learning rate of 0.01.
- Perform minimization using the loss function, loss_function(), and the variable with an initial value of 6.0, x_1.
- Perform minimization using the loss function, loss_function(), and the variable with an initial value of 0.3, x_2.
- Print x_1 and x_2 as numpy arrays and check whether the values differ. These are the minima that the algorithm identified.
'''

# Initialize x_1 and x_2
x_1 = Variable(6.0,float32)
x_2 = Variable(0.3,float32)

# Define the optimization operation
opt = keras.optimizers.SGD(learning_rate=0.01)

for j in range(100):
	# Perform minimization using the loss function and x_1
	opt.minimize(lambda: loss_function(x_1), var_list=[x_1])
	# Perform minimization using the loss function and x_2
	opt.minimize(lambda: loss_function(x_2), var_list=[x_2])

# Print x_1 and x_2 as numpy arrays
print(x_1.numpy(), x_2.numpy())
