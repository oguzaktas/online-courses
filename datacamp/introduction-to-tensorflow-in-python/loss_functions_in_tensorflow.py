'''
Loss functions
Higher value -> worse fit: Minimize the loss function
Common loss functions in TensorFlow: MSE, MAE, huber error
tf.keras.losses.mse(), tf.keras.losses.mae(), tf.keras.losses.Huber()
'''

'''
Instructions
- Import the keras module from tensorflow. Then, use price and predictions to compute the mean squared error (mse).
- Modify your code to compute the mean absolute error (mae), rather than the mean squared error (mse).
'''

# Import the keras module from tensorflow
from tensorflow import keras

# Compute the mean squared error (mse)
loss = keras.losses.mse(price, predictions)

# Compute the mean absolute error (mae)
loss = keras.losses.mae(price, predictions)

# Print the mean squared error (mse)
print(loss.numpy())
