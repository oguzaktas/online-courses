'''
Overview of training and evaluation
1. Load and clean data
2. Define model
3. Train and validate model
4. Evaluate model
Training model the fit() operation required arguments -> features, labels
Some of optional arguments for fit() operation -> batch_size, epochs, validation_split
'''

'''
Instructions
- Define a sequential model named model.
- Set the output layer to be dense, have 4 nodes, and use a softmax activation function.
- Compile the model with the SGD optimizer and categorical_crossentropy loss.
- Complete the fitting operation and set the number of epochs to 5.
'''

# Define a sequential model
model = keras.Sequential()

# Define a hidden layer
model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))

# Define the output layer
model.add(keras.layers.Dense(4, activation='softmax'))

# Compile the model
model.compile('SGD', loss='categorical_crossentropy')

# Complete the fitting operation
model.fit(sign_language_features, sign_language_labels, epochs=5)

'''
Output:
Train on 1000 samples
Epoch 1/5

  32/1000 [..............................] - ETA: 15s - loss: 1.3557
 576/1000 [================>.............] - ETA: 0s - loss: 1.2926 
1000/1000 [==============================] - 1s 603us/sample - loss: 1.2597
Epoch 2/5

  32/1000 [..............................] - ETA: 0s - loss: 1.2320
 608/1000 [=================>............] - ETA: 0s - loss: 1.1539
1000/1000 [==============================] - 0s 92us/sample - loss: 1.1214
Epoch 3/5

  32/1000 [..............................] - ETA: 0s - loss: 1.2827
 704/1000 [====================>.........] - ETA: 0s - loss: 0.9924
1000/1000 [==============================] - 0s 81us/sample - loss: 0.9672
Epoch 4/5

  32/1000 [..............................] - ETA: 0s - loss: 0.9412
 640/1000 [==================>...........] - ETA: 0s - loss: 0.8681
1000/1000 [==============================] - 0s 85us/sample - loss: 0.8590
Epoch 5/5

  32/1000 [..............................] - ETA: 0s - loss: 1.1681
 768/1000 [======================>.......] - ETA: 0s - loss: 0.7752
1000/1000 [==============================] - 0s 71us/sample - loss: 0.7637
Out[1]: <tensorflow.python.keras.callbacks.History at 0x7f87b447d7b8>
'''