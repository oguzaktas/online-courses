'''
Instructions
- Create a Sequential model.
- Add a dense layer with as many neurons as the encoded image dimensions and input_shape the original size of the image.
- Add a final layer with as many neurons as pixels in the input images.
- Compile your autoencoder using adadelta as an optimizer and binary_crossentropy loss, then summarise it.
'''

# Start with a sequential model
autoencoder = Sequential()

# Add a dense layer with the original image as input
autoencoder.add(Dense(32, input_shape=(784, ), activation="relu"))

# Add an output layer with as many nodes as the image
autoencoder.add(Dense(784, activation="sigmoid"))

# Compile your model
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

# Take a look at your model structure
autoencoder.summary()

'''
Output;

<script.py> output:
    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense_1 (Dense)              (None, 32)                25120     
    _________________________________________________________________
    dense_2 (Dense)              (None, 784)               25872     
    =================================================================
    Total params: 50,992
    Trainable params: 50,992
    Non-trainable params: 0
    _________________________________________________________________
'''