'''
Instructions
- Import both the EarlyStopping and ModelCheckpoint callbacks from keras.
- Create monitor_val_acc as an EarlyStopping callback that will monitor 'val_acc', with a patience of 3 epochs.
- Create modelCheckpoint as a ModelCheckpointcallback, save the best model as best_banknote_model.hdf5.
- Fit your model providing a list with the defined callbacks and X_test and y_test as validation data.
'''

# Import the EarlyStopping and ModelCheckpoint callbacks
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Early stop on validation accuracy
monitor_val_acc = EarlyStopping(monitor = 'val_acc', patience=3)

# Save the best model as best_banknote_model.hdf5
modelCheckpoint = ModelCheckpoint('best_banknote_model.hdf5', save_best_only = True)

# Fit your model for a stupid amount of epochs
history = model.fit(X_train, y_train,
                    epochs = 10000000,
                    callbacks = [monitor_val_acc, modelCheckpoint],
                    validation_data = (X_test, y_test))

'''
Output;

<script.py> output:
    Train on 960 samples, validate on 412 samples
    Epoch 1/10000000
    
     32/960 [>.............................] - ETA: 2s - loss: 0.3227 - acc: 0.8438
    960/960 [==============================] - 0s 148us/step - loss: 0.2829 - acc: 0.9250 - val_loss: 0.3030 - val_acc: 0.9126
    Epoch 2/10000000
    
     32/960 [>.............................] - ETA: 0s - loss: 0.2523 - acc: 0.9688
    960/960 [==============================] - 0s 54us/step - loss: 0.2776 - acc: 0.9271 - val_loss: 0.2973 - val_acc: 0.9126
    Epoch 3/10000000
    
     32/960 [>.............................] - ETA: 0s - loss: 0.2336 - acc: 0.9688
    960/960 [==============================] - 0s 54us/step - loss: 0.2726 - acc: 0.9292 - val_loss: 0.2920 - val_acc: 0.9126
    Epoch 4/10000000
    
     32/960 [>.............................] - ETA: 0s - loss: 0.2699 - acc: 0.9688
    960/960 [==============================] - 0s 54us/step - loss: 0.2679 - acc: 0.9312 - val_loss: 0.2870 - val_acc: 0.9126
'''