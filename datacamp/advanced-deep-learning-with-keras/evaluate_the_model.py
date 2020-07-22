'''
Instructions
- Evaluate the model on the games_tourney_test data.
- Recall that the model's inputs are 'home', 'seed_diff', and 'prediction' columns and the target column is 'score_diff'.
'''

# Evaluate the model on the games_tourney_test dataset
print(model.evaluate(games_tourney_test[['home', 'seed_diff', 'prediction']],
               games_tourney_test['score_diff'], verbose=False))

'''
Output:
<script.py> output:
    9.07315489498804
'''                   