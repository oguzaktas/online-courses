'''
Instructions
- Evaluate the model on games_tourney_test.
- Use the same inputs and outputs as the training set.
'''

# Evaluate the model on new data
print(model.evaluate(games_tourney_test[['seed_diff', 'pred']],
               [games_tourney_test[['score_diff']], games_tourney_test[['won']]], verbose=False))

'''
Output:
In [1]: # Evaluate the model on new data
        print(model.evaluate(games_tourney_test[['seed_diff', 'pred']],
                       [games_tourney_test[['score_diff']], games_tourney_test[['won']]], verbose=False))
[9.685116468970456, 9.11585681592647, 0.5692595753503676]
'''