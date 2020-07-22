'''
Instructions
- Load the weights from a file called 'weights.hdf5'.
- Predict the classes of the first three images from test_data.
'''

# Load the weights from file
model.load_weights('weights.hdf5')

# Predict from the first three images in the test data
model.predict(test_data[0:3])
