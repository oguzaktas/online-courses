'''
Instructions
- Define a sequential model in keras named model.
- Add a first dense layer with 1024 nodes, a relu activation, and an input shape of (784,).
- Set the learning rate to 0.001.
- Set the fit() operation to iterate over the full sample 50 times and use 50% of the sample for validation purposes.
'''

# Define sequential model
model = keras.Sequential()

# Define the first layer
model.add(keras.layers.Dense(1024, activation='relu', input_shape=(784,)))

# Add activation function to classifier
model.add(keras.layers.Dense(4, activation='softmax'))

# Finish the model compilation
model.compile(optimizer=keras.optimizers.Adam(lr=0.001), 
              loss='categorical_crossentropy', metrics=['accuracy'])

# Complete the model fit operation
model.fit(sign_language_features, sign_language_labels, epochs=50, validation_split=0.5)

'''
Output:
Train on 13 samples, validate on 13 samples
Epoch 1/50

13/13 [==============================] - 1s 56ms/sample - loss: 1.3461 - accuracy: 0.3077 - val_loss: 3.0842 - val_accuracy: 0.3846
Epoch 2/50

13/13 [==============================] - 0s 1ms/sample - loss: 2.4663 - accuracy: 0.2308 - val_loss: 4.2784 - val_accuracy: 0.3846
Epoch 3/50

13/13 [==============================] - 0s 962us/sample - loss: 2.1878 - accuracy: 0.6154 - val_loss: 5.6272 - val_accuracy: 0.3077
Epoch 4/50

13/13 [==============================] - 0s 904us/sample - loss: 3.6705 - accuracy: 0.3846 - val_loss: 4.5968 - val_accuracy: 0.3077
Epoch 5/50

13/13 [==============================] - 0s 968us/sample - loss: 2.5616 - accuracy: 0.6923 - val_loss: 4.3052 - val_accuracy: 0.0769
Epoch 6/50

13/13 [==============================] - 0s 983us/sample - loss: 2.3775 - accuracy: 0.6154 - val_loss: 2.8193 - val_accuracy: 0.0769
Epoch 7/50

13/13 [==============================] - 0s 966us/sample - loss: 1.5247 - accuracy: 0.6154 - val_loss: 1.0500 - val_accuracy: 0.5385
Epoch 8/50

13/13 [==============================] - 0s 934us/sample - loss: 0.6675 - accuracy: 0.7692 - val_loss: 0.9406 - val_accuracy: 0.6154
Epoch 9/50

13/13 [==============================] - 0s 903us/sample - loss: 1.2254 - accuracy: 0.5385 - val_loss: 1.1072 - val_accuracy: 0.4615
Epoch 10/50

13/13 [==============================] - 0s 870us/sample - loss: 1.6209 - accuracy: 0.5385 - val_loss: 0.9477 - val_accuracy: 0.6923
Epoch 11/50

13/13 [==============================] - 0s 879us/sample - loss: 1.3329 - accuracy: 0.5385 - val_loss: 0.8459 - val_accuracy: 0.6923
Epoch 12/50

13/13 [==============================] - 0s 887us/sample - loss: 0.8220 - accuracy: 0.6154 - val_loss: 1.0359 - val_accuracy: 0.5385
Epoch 13/50

13/13 [==============================] - 0s 874us/sample - loss: 0.5389 - accuracy: 0.8462 - val_loss: 1.5257 - val_accuracy: 0.3846
Epoch 14/50

13/13 [==============================] - 0s 889us/sample - loss: 0.6948 - accuracy: 0.6923 - val_loss: 2.0301 - val_accuracy: 0.3846
Epoch 15/50

13/13 [==============================] - 0s 913us/sample - loss: 0.9550 - accuracy: 0.6923 - val_loss: 2.0480 - val_accuracy: 0.3846
Epoch 16/50

13/13 [==============================] - 0s 909us/sample - loss: 0.9436 - accuracy: 0.6923 - val_loss: 1.6047 - val_accuracy: 0.3846
Epoch 17/50

13/13 [==============================] - 0s 919us/sample - loss: 0.6777 - accuracy: 0.6923 - val_loss: 1.1002 - val_accuracy: 0.4615
Epoch 18/50

13/13 [==============================] - 0s 935us/sample - loss: 0.4211 - accuracy: 0.8462 - val_loss: 0.8775 - val_accuracy: 0.6923
Epoch 19/50

13/13 [==============================] - 0s 909us/sample - loss: 0.4486 - accuracy: 0.8462 - val_loss: 0.8258 - val_accuracy: 0.6923
Epoch 20/50

13/13 [==============================] - 0s 914us/sample - loss: 0.6064 - accuracy: 0.6154 - val_loss: 0.7554 - val_accuracy: 0.6923
Epoch 21/50

13/13 [==============================] - 0s 916us/sample - loss: 0.6040 - accuracy: 0.6154 - val_loss: 0.6710 - val_accuracy: 0.7692
Epoch 22/50

13/13 [==============================] - 0s 908us/sample - loss: 0.4510 - accuracy: 0.7692 - val_loss: 0.7021 - val_accuracy: 0.7692
Epoch 23/50

13/13 [==============================] - 0s 908us/sample - loss: 0.3448 - accuracy: 1.0000 - val_loss: 0.8841 - val_accuracy: 0.6154
Epoch 24/50

13/13 [==============================] - 0s 915us/sample - loss: 0.3646 - accuracy: 1.0000 - val_loss: 1.0934 - val_accuracy: 0.4615
Epoch 25/50

13/13 [==============================] - 0s 930us/sample - loss: 0.4279 - accuracy: 0.7692 - val_loss: 1.1553 - val_accuracy: 0.4615
Epoch 26/50

13/13 [==============================] - 0s 897us/sample - loss: 0.4289 - accuracy: 0.6923 - val_loss: 1.0227 - val_accuracy: 0.5385
Epoch 27/50

13/13 [==============================] - 0s 922us/sample - loss: 0.3458 - accuracy: 0.6923 - val_loss: 0.8419 - val_accuracy: 0.6923
Epoch 28/50

13/13 [==============================] - 0s 902us/sample - loss: 0.2693 - accuracy: 0.9231 - val_loss: 0.7599 - val_accuracy: 0.6923
Epoch 29/50

13/13 [==============================] - 0s 939us/sample - loss: 0.2741 - accuracy: 0.9231 - val_loss: 0.7528 - val_accuracy: 0.6923
Epoch 30/50

13/13 [==============================] - 0s 936us/sample - loss: 0.3189 - accuracy: 0.8462 - val_loss: 0.7428 - val_accuracy: 0.7692
Epoch 31/50

13/13 [==============================] - 0s 865us/sample - loss: 0.3236 - accuracy: 0.8462 - val_loss: 0.7158 - val_accuracy: 0.6923
Epoch 32/50

13/13 [==============================] - 0s 861us/sample - loss: 0.2771 - accuracy: 0.9231 - val_loss: 0.7075 - val_accuracy: 0.6923
Epoch 33/50

13/13 [==============================] - 0s 893us/sample - loss: 0.2321 - accuracy: 1.0000 - val_loss: 0.7444 - val_accuracy: 0.6923
Epoch 34/50

13/13 [==============================] - 0s 951us/sample - loss: 0.2246 - accuracy: 1.0000 - val_loss: 0.8045 - val_accuracy: 0.6154
Epoch 35/50

13/13 [==============================] - 0s 906us/sample - loss: 0.2386 - accuracy: 1.0000 - val_loss: 0.8353 - val_accuracy: 0.5385
Epoch 36/50

13/13 [==============================] - 0s 887us/sample - loss: 0.2408 - accuracy: 1.0000 - val_loss: 0.8052 - val_accuracy: 0.5385
Epoch 37/50

13/13 [==============================] - 0s 885us/sample - loss: 0.2196 - accuracy: 1.0000 - val_loss: 0.7360 - val_accuracy: 0.6923
Epoch 38/50

13/13 [==============================] - 0s 918us/sample - loss: 0.1944 - accuracy: 1.0000 - val_loss: 0.6752 - val_accuracy: 0.6923
Epoch 39/50

13/13 [==============================] - 0s 987us/sample - loss: 0.1877 - accuracy: 1.0000 - val_loss: 0.6398 - val_accuracy: 0.7692
Epoch 40/50

13/13 [==============================] - 0s 914us/sample - loss: 0.1952 - accuracy: 1.0000 - val_loss: 0.6147 - val_accuracy: 0.7692
Epoch 41/50

13/13 [==============================] - 0s 917us/sample - loss: 0.1948 - accuracy: 1.0000 - val_loss: 0.5950 - val_accuracy: 0.7692
Epoch 42/50

13/13 [==============================] - 0s 911us/sample - loss: 0.1787 - accuracy: 1.0000 - val_loss: 0.5959 - val_accuracy: 0.7692
Epoch 43/50

13/13 [==============================] - 0s 909us/sample - loss: 0.1610 - accuracy: 1.0000 - val_loss: 0.6252 - val_accuracy: 0.7692
Epoch 44/50

13/13 [==============================] - 0s 924us/sample - loss: 0.1552 - accuracy: 1.0000 - val_loss: 0.6674 - val_accuracy: 0.7692
Epoch 45/50

13/13 [==============================] - 0s 923us/sample - loss: 0.1578 - accuracy: 1.0000 - val_loss: 0.6989 - val_accuracy: 0.7692
Epoch 46/50

13/13 [==============================] - 0s 929us/sample - loss: 0.1573 - accuracy: 1.0000 - val_loss: 0.7078 - val_accuracy: 0.6923
Epoch 47/50

13/13 [==============================] - 0s 889us/sample - loss: 0.1495 - accuracy: 1.0000 - val_loss: 0.6976 - val_accuracy: 0.6923
Epoch 48/50

13/13 [==============================] - 0s 907us/sample - loss: 0.1394 - accuracy: 1.0000 - val_loss: 0.6791 - val_accuracy: 0.7692
Epoch 49/50

13/13 [==============================] - 0s 882us/sample - loss: 0.1334 - accuracy: 1.0000 - val_loss: 0.6602 - val_accuracy: 0.6923
Epoch 50/50

13/13 [==============================] - 0s 908us/sample - loss: 0.1323 - accuracy: 1.0000 - val_loss: 0.6412 - val_accuracy: 0.6923
Out[1]: <tensorflow.python.keras.callbacks.History at 0x7f878c5bc6d8>
'''