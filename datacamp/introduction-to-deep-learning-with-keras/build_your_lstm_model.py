'''
Instructions
- Import the Embedding, LSTM and Dense layer from Keras layers.
- Add an Embedding() layer of the vocabulary size, that will encode words into 8 number vectors and receive sequences of length 3.
- Add a 32 unit LSTM() layer.
- Add a hidden Dense() layer of 32 units and an output layer of vocab_size with softmax.
'''

# Import the Embedding, LSTM and Dense layer
from keras.layers import Embedding, LSTM, Dense

model = Sequential()

# Add an Embedding layer with the right parameters
model.add(Embedding(input_dim=vocab_size, output_dim=8, input_length=3))

# Add a 32 unit LSTM layer
model.add(LSTM(32))

# Add a hidden Dense layer of 32 units and an output layer of vocab_size with softmax
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='softmax'))
model.summary()

'''
Output;

<script.py> output:
    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    embedding_1 (Embedding)      (None, 3, 8)              352       
    _________________________________________________________________
    lstm_1 (LSTM)                (None, 32)                5248      
    _________________________________________________________________
    dense_1 (Dense)              (None, 32)                1056      
    _________________________________________________________________
    dense_2 (Dense)              (None, 32)                1056      
    =================================================================
    Total params: 7,712
    Trainable params: 7,712
    Non-trainable params: 0
    _________________________________________________________________
'''