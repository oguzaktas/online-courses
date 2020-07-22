'''
Instructions
- Use get_model() to get a new, already compiled, model, then train your model for 5 epochs with a batch_size of 1.
- Now train a new model with batch_size equal to the size of the training set.
'''

model = get_model()

# Fit your model for 5 epochs with a batch of size the training set
model.fit(X_train, y_train, epochs=5, ____=____)
print("\n The accuracy when using the whole training set as a batch was: ",
      model.evaluate(X_test, y_test)[1])

'''
Output;

<script.py> output:
    Epoch 1/5
    
    700/700 [==============================] - 0s 194us/step - loss: 0.6730 - acc: 0.4786
    Epoch 2/5
    
    700/700 [==============================] - 0s 3us/step - loss: 0.6728 - acc: 0.4786
    Epoch 3/5
    
    700/700 [==============================] - 0s 2us/step - loss: 0.6727 - acc: 0.4786
    Epoch 4/5
    
    700/700 [==============================] - 0s 3us/step - loss: 0.6725 - acc: 0.4786
    Epoch 5/5
    
    700/700 [==============================] - 0s 2us/step - loss: 0.6723 - acc: 0.4786
    
     32/300 [==>...........................] - ETA: 0s
    300/300 [==============================] - 0s 86us/step
    
     The accuracy when using the whole training set as a batch was:  0.553333334128062
'''