'''
Instructions
- Import the Sequential model from keras.models and the Denselayer from keras.layers.
- Create an instance of the Sequential model.
- Add a 10-neuron hidden Dense layer with an input_shape of two neurons.
- Add a final 1-neuron output layer and summarize your model with summary().
'''

# Import the Sequential model and Dense layer
from keras.models import Sequential
from keras.layers import Dense

# Create a Sequential model
model = Sequential()

# Add an input layer and a hidden layer with 10 neurons
model.add(Dense(10, input_shape=(2,), activation="relu"))

# Add a 1-neuron output layer
model.add(Dense(1))

# Summarise your model
model.summary()

'''
Output;
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 10)                30        
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 11        
=================================================================
Total params: 41
Trainable params: 41
Non-trainable params: 0
_________________________________________________________________
'''