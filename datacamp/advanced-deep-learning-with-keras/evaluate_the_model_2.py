'''
Instructions
- Evaluate the model on games_tourney_test.
- Use the same inputs and outputs as the training set.
'''

# Evaluate the model on the tournament test data
print(model.evaluate(games_tourney_test[['seed_diff', 'pred']], games_tourney_test[['score_1', 'score_2']], verbose=False))

'''
Output:
<script.py> output:
    8.986760239102948
'''    