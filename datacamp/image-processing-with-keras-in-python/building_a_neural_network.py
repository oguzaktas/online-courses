'''
Instructions
- The first layer receives images as input, has 10 units and 'relu' activation.
- The second input layer has 10 units and 'relu' activation.
- The output layer has one unit for each category (3 categories) and 'softmax' activation.
'''

# Imports components from Keras
from keras.models import Sequential
from keras.layers import Dense

# Initializes a sequential model
model = Sequential()

# First layer
model.add(Dense(10, activation='relu', input_shape=(784,)))

# Second layer
model.add(Dense(10, activation='relu'))

# Output layer
model.add(Dense(3, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', 
           loss='categorical_crossentropy', 
           metrics=['accuracy'])

# Reshape the data to two-dimensional array
train_data = train_data.reshape(50, 784)

# Fit the model
model.fit(train_data, train_labels, validation_split=0.2, epochs=3)

# Reshape test data
test_data = test_data.reshape(50, 784)

# Evaluate the model
model.evaluate(test_data, test_labels)
