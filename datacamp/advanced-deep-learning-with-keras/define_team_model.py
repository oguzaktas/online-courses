'''
Instructions
- Create a 1D input layer for the team ID (which will be an integer). Be sure to set the correct input shape!
- Pass this input to the team strength lookup layer you created previously.
- Flatten the output of the team strength lookup.
- Create a model that uses the 1D input as input and flattened team strength as output.
'''

# Imports
from keras.layers import Input, Embedding, Flatten
from keras.models import Model

# Create an input layer for the team ID
teamid_in = Input(shape=(1,))

# Lookup the input in the team strength embedding layer
strength_lookup = team_lookup(teamid_in)

# Flatten the output
strength_lookup_flat = Flatten()(strength_lookup)

# Combine the operations into a single, re-usable model
team_strength_model = Model(teamid_in, strength_lookup_flat, name='Team-Strength-Model')