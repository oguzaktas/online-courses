'''
Instructions
- Assign the 'team_1' and 'team_2' columns from games_season to input_1 and input_2, respectively.
- Use 'score_diff' column from games_season as the target.
- Fit the model using 1 epoch, a batch size of 2048, and a 10% validation split.
'''

# Get the team_1 column from the regular season data
input_1 = games_season['team_1']

# Get the team_2 column from the regular season data
input_2 = games_season['team_2']

# Fit the model to input 1 and 2, using score diff as a target
model.fit([input_1, input_2],
          games_season['score_diff'],
          epochs=1,
          batch_size=2048,
          validation_split=0.1,
          verbose=True)

'''
Output:
<script.py> output:
    Train on 280960 samples, validate on 31218 samples
    Epoch 1/1
    
      2048/280960 [..............................] - ETA: 10s - loss: 12.0254
     40960/280960 [===>..........................] - ETA: 0s - loss: 12.1970 
     79872/280960 [=======>......................] - ETA: 0s - loss: 12.1440
    118784/280960 [===========>..................] - ETA: 0s - loss: 12.1133
    157696/280960 [===============>..............] - ETA: 0s - loss: 12.1358
    196608/280960 [===================>..........] - ETA: 0s - loss: 12.1249
    235520/280960 [========================>.....] - ETA: 0s - loss: 12.1275
    274432/280960 [============================>.] - ETA: 0s - loss: 12.1246
    280960/280960 [==============================] - 0s 2us/step - loss: 12.1203 - val_loss: 11.8384
'''              