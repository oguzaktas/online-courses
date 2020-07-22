'''
Instructions
- Fit the model to the games_tourney_train dataset using 1 epoch.
- The input columns are 'home', 'seed_diff', and 'pred'.
- The target column is 'score_diff'.
'''

# Fit the model
model.fit(games_tourney_train[['home', 'seed_diff', 'pred']],
          games_tourney_train['score_diff'],
          epochs=1,
          verbose=True)

'''
Output:
<script.py> output:
    Epoch 1/1
    
      32/3168 [..............................] - ETA: 11s - loss: 21.2439
     832/3168 [======>.......................] - ETA: 0s - loss: 18.4599 
    1632/3168 [==============>...............] - ETA: 0s - loss: 18.3717
    2400/3168 [=====================>........] - ETA: 0s - loss: 18.1251
    3168/3168 [==============================] - 0s 101us/step - loss: 17.8147
'''