'''
Instructions
- Use the model to predict on the games_tourney dataset. The model has three inputs: 'team_1', 'team_2', and 'home' columns. Assign the predictions to a new column, 'pred'
'''

# Predict
games_tourney['pred'] = model.predict([games_tourney['team_1'], games_tourney['team_2'], games_tourney['home']])