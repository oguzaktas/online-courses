'''
Instructions
- Assign the 'team_1' and 'team_2' columns from games_tourney to input_1 and input_2, respectively.
- Evaluate the model.
'''

# Get team_1 from the tournament data
input_1 = games_tourney['team_1']

# Get team_2 from the tournament data
input_2 = games_tourney['team_2']

# Evaluate the model using these inputs
print(model.evaluate([input_1, input_2], games_tourney['score_diff'], verbose=False))

'''
Output:
11.649009290595183
'''