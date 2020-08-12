'''
- Import Adam from keras.optimizers.
- Compile the model with 2 losses: 'mean_absolute_error' and 'binary_crossentropy', and use the Adam optimizer with a learning rate of 0.01.
- Fit the model with 'seed_diff' and 'pred' columns as the inputs and 'score_diff' and 'won' columns as the targets.
- Use 10 epochs and a batch size of 16384.
'''

# Import the Adam optimizer
from keras.optimizers import Adam

# Compile the model with 2 losses and the Adam optimzer with a higher learning rate
model.compile(loss=['mean_absolute_error', 'binary_crossentropy'], optimizer=Adam(lr=0.01))

# Fit the model to the tournament training data, with 2 inputs and 2 outputs
model.fit(games_tourney_train[['seed_diff', 'pred']],
          [games_tourney_train[['score_diff']], games_tourney_train[['won']]],
          epochs=10,
          verbose=True,
          batch_size=16384)

'''
Output:
Epoch 1/10

3430/3430 [==============================] - 0s 38us/step - loss: 9.5718 - dense_1_loss: 8.9779 - dense_2_loss: 0.5939
Epoch 2/10

3430/3430 [==============================] - 0s 2us/step - loss: 9.5688 - dense_1_loss: 8.9761 - dense_2_loss: 0.5927
Epoch 3/10

3430/3430 [==============================] - 0s 2us/step - loss: 9.5658 - dense_1_loss: 8.9743 - dense_2_loss: 0.5915
Epoch 4/10

3430/3430 [==============================] - 0s 1us/step - loss: 9.5629 - dense_1_loss: 8.9726 - dense_2_loss: 0.5903
Epoch 5/10

3430/3430 [==============================] - 0s 2us/step - loss: 9.5600 - dense_1_loss: 8.9708 - dense_2_loss: 0.5891
Epoch 6/10

3430/3430 [==============================] - 0s 1us/step - loss: 9.5571 - dense_1_loss: 8.9692 - dense_2_loss: 0.5880
Epoch 7/10

3430/3430 [==============================] - 0s 1us/step - loss: 9.5543 - dense_1_loss: 8.9675 - dense_2_loss: 0.5868
Epoch 8/10

3430/3430 [==============================] - 0s 1us/step - loss: 9.5516 - dense_1_loss: 8.9659 - dense_2_loss: 0.5857
Epoch 9/10

3430/3430 [==============================] - 0s 1us/step - loss: 9.5489 - dense_1_loss: 8.9644 - dense_2_loss: 0.5846
Epoch 10/10

3430/3430 [==============================] - 0s 1us/step - loss: 9.5464 - dense_1_loss: 8.9629 - dense_2_loss: 0.5834
Out[1]: <keras.callbacks.History at 0x7fa89e243a20>          
'''