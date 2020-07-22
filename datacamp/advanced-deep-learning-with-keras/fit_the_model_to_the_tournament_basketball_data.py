'''
Instructions
- Fit the model with seed_diff as the input variable and score_diff as the output variable.
- Use 1 epoch, a batch size of 128, and a 10% validation split.
'''

# Now fit the model
model.fit(games_tourney_train['seed_diff'], games_tourney_train['score_diff'],
          epochs=1,
          batch_size=128,
          validation_split=0.1,
          verbose=True)

'''
Output:
Train on 3087 samples, validate on 343 samples
Epoch 1/1

 128/3087 [>.............................] - ETA: 3s - loss: 12.6147
2560/3087 [=======================>......] - ETA: 0s - loss: 12.6966
3087/3087 [==============================] - 0s 66us/step - loss: 12.6617 - val_loss: 11.8746
Out[1]: <keras.callbacks.History at 0x7f376365e5c0>
'''