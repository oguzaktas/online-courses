'''
Instructions
- Pass model 1's input layer to its first layer and model 1's first layer to its second layer.
- Pass model 2's input layer to its first layer and model 2's first layer to its second layer.
- Use the add() operation to combine the second layers of model 1 and model 2.
- Complete the functional model definition.
'''

# For model 1, pass the input layer to layer 1 and layer 1 to layer 2
m1_layer1 = keras.layers.Dense(12, activation='sigmoid')(m1_inputs)
m1_layer2 = keras.layers.Dense(4, activation='softmax')(m1_layer1)

# For model 2, pass the input layer to layer 1 and layer 1 to layer 2
m2_layer1 = keras.layers.Dense(12, activation='relu')(m2_inputs)
m2_layer2 = keras.layers.Dense(4, activation='softmax')(m2_layer1)

# Merge model outputs and define a functional model
merged = keras.layers.add([m1_layer2, m2_layer2])
model = keras.Model(inputs=[m1_inputs, m2_inputs], outputs=merged)

# Print a model summary
print(model.summary())

'''
Output:
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            [(None, 784)]        0                                            
__________________________________________________________________________________________________
input_2 (InputLayer)            [(None, 784)]        0                                            
__________________________________________________________________________________________________
dense (Dense)                   (None, 12)           9420        input_1[0][0]                    
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 12)           9420        input_2[0][0]                    
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 4)            52          dense[0][0]                      
__________________________________________________________________________________________________
dense_3 (Dense)                 (None, 4)            52          dense_2[0][0]                    
__________________________________________________________________________________________________
add (Add)                       (None, 4)            0           dense_1[0][0]                    
                                                                 dense_3[0][0]                    
==================================================================================================
Total params: 18,944
Trainable params: 18,944
Non-trainable params: 0
__________________________________________________________________________________________________
None
'''