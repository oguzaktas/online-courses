'''
Instructions
- Set the learning rate of the Adam optimizer to the one passed in the parameters.
- Set the hidden layers activations to the one passed in the parameters.
- Pass the optimizer and the binary cross-entropy loss to the .compile() method.
'''

# Creates a model given an activation and learning rate
def create_model(learning_rate=0.01, activation='relu'):
  
  	# Create an Adam optimizer with the given learning rate
  	opt = Adam(lr=learning_rate)
  	
  	# Create your binary classification model  
  	model = Sequential()
  	model.add(Dense(128, input_shape=(30,), activation='relu'))
  	model.add(Dense(256, activation='relu'))
  	model.add(Dense(1, activation='sigmoid'))
  	
  	# Compile your model with your optimizer, loss, and metrics
  	model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
  	return model
