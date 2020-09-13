'''
Instructions
- Assign the test data (seed_diff column) to X_test.
- Assign the target data (score_diff column) to y_test.
- Evaluate the model on X_test and y_test.
'''

# Load the X variable from the test data
X_test = games_tourney_test['seed_diff']

# Load the y variable from the test data
y_test = games_tourney_test['score_diff']

# Evaluate the model on the test data
print(model.evaluate(X_test, y_test, verbose=False))

'''
Output:
10.06973339669147
'''