'''
Instructions
- Instantiate a new Sequential() model.
- Add a Dense() layer with five neurons and three neurons as input.
- Add a final dense layer with one neuron and no activation.

'''

# Import the Sequential model and Dense layer
from keras.models import Sequential
from keras.layers import Dense

# Instantiate a new Sequential model
model = Sequential()

# Add a Dense layer with five neurons and three inputs
model.add(Dense(5, input_shape=(3,), activation="relu"))

# Add a final Dense layer with one neuron and no activation
model.add(Dense(1))

# Summarize your model
model.summary()

'''
Output;
<script.py> output:
    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense_1 (Dense)              (None, 5)                 20        
    _________________________________________________________________
    dense_2 (Dense)              (None, 1)                 6         
    =================================================================
    Total params: 26
    Trainable params: 26
    Non-trainable params: 0
    _________________________________________________________________
'''