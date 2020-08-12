'''
Instructions
- Create a model using team_in_1, team_in_2, and home_in as inputs and out as the output.
- Compile the model using the 'adam' optimizer and 'mean_absolute_error' as the loss function.
'''

# Import the model class
from keras.models import Model

# Make a Model
model = Model([team_in_1, team_in_2, home_in], out)

# Compile the model
model.compile(optimizer='adam', loss='mean_absolute_error')