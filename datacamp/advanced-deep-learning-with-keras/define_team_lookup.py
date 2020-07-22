'''
Instructions
- Count the number of unique teams.
- Create an embedding layer that maps each team ID to a single number representing that team's strength.
- The output shape should be 1 dimension (as we want to represent the teams by a single number).
- The input length should be 1 dimension (as each team is represented by exactly one id).
'''

# Imports
from keras.layers import Embedding
from numpy import unique

# Count the unique number of teams
n_teams = unique(games_season['team_1']).shape[0]

# Create an embedding layer
team_lookup = Embedding(input_dim=n_teams,
                        output_dim=1,
                        input_length=1,
                        name='Team-Strength')