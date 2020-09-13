'''
Instructions
- Fit the model to the games_tourney_train dataset using 100 epochs and a batch size of 16384.
- The input columns are 'seed_diff', and 'pred'.
- The target columns are 'score_1' and 'score_2'.
'''

# Fit the model
model.fit(games_tourney_train[['seed_diff', 'pred']],
  		  games_tourney_train[['score_1', 'score_2']],
  		  verbose=True,
  		  epochs=100,
  		  batch_size=16384)