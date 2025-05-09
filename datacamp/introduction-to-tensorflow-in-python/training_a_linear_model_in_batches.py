'''
Instructions
- Use the .Adam() optimizer.
- Load in the data from 'kc_house_data.csv' in batches with a chunksize of 100.
- Extract the price column from batch, convert it to a numpy array of type 32-bit float, and assign it to price_batch.
- Complete the loss function, fill in the list of trainable variables, and perform minimization.
'''

# Initialize adam optimizer
opt = keras.optimizers.Adam()

# Load data in batches
for batch in pd.read_csv('kc_house_data.csv', chunksize=100):
	size_batch = np.array(batch['sqft_lot'], np.float32)

	# Extract the price values for the current batch
	price_batch = np.array(batch['price'], np.float32)

	# Complete the loss, fill in the variable list, and minimize
	opt.minimize(lambda: loss_function(intercept, slope, price_batch, size_batch), var_list=[intercept, slope])

# Print trained parameters
print(intercept.numpy(), slope.numpy())
