'''
Instructions
- Instantiate a Sequential model.
- Add 3 dense layers of 128, 64 and 32 neurons each.
- Add a final dense layer with as many neurons as competitors.
- Compile your model using categorical_crossentropy loss.
'''

# Instantiate a sequential model
model = Sequential()
  
# Add 3 dense layers of 128, 64 and 32 neurons each
model.add(Dense(128, input_shape=(2,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
  
# Add a dense layer with as many neurons as competitors
model.add(Dense(4, activation='softmax'))
  
# Compile your model using categorical_crossentropy loss
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])