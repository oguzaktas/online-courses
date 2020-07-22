'''
Instructions
- Fit the model to the games_season dataset, using 'team_1', 'team_2' and 'home' columns as inputs, and the 'score_diff' column as the target.
- Fit the model using 1 epoch, 10% validation split and a batch size of 2048.
- Evaluate the model on games_tourney, using the same inputs and outputs.
'''

# Fit the model to the games_season dataset
model.fit([games_season['team_1'], games_season['team_2'], games_season['home']],
          games_season['score_diff'],
          epochs=1,
          verbose=True,
          validation_split=0.1,
          batch_size=2048)

# Evaluate the model on the games_tourney dataset
print(model.evaluate([games_tourney['team_1'], games_tourney['team_2'], games_tourney['home']], games_tourney['score_diff'], verbose=False))

'''
Output:
<script.py> output:
    Train on 280960 samples, validate on 31218 samples
    Epoch 1/1
    
      2048/280960 [..............................] - ETA: 16s - loss: 12.0596
     34816/280960 [==>...........................] - ETA: 1s - loss: 11.9955 
     67584/280960 [======>.......................] - ETA: 0s - loss: 12.0207
    100352/280960 [=========>....................] - ETA: 0s - loss: 11.9886
    133120/280960 [=============>................] - ETA: 0s - loss: 12.0237
    165888/280960 [================>.............] - ETA: 0s - loss: 12.0137
    198656/280960 [====================>.........] - ETA: 0s - loss: 12.0248
    231424/280960 [=======================>......] - ETA: 0s - loss: 12.0196
    264192/280960 [===========================>..] - ETA: 0s - loss: 12.0036
    280960/280960 [==============================] - 1s 2us/step - loss: 12.0003 - val_loss: 12.3391
    11.683795701010249
 '''   