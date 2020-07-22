'''
Instructions
- Convert df.survived to a categorical variable using the to_categorical() function.
- Specify a Sequential model called model.
- Add a Dense layer with 32 nodes. Use 'relu' as the activation and (n_cols,) as the input_shape.
- Add the Dense output layer. Because there are two outcomes, it should have 2 units, 
and because it is a classification model, the activation should be 'softmax'.
- Compile the model, using 'sgd' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] 
to see the accuracy (what fraction of predictions were correct) at the end of each epoch.
- Fit the model using the predictors and the target.
'''

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))

# Add the output layer
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(predictors, target)
