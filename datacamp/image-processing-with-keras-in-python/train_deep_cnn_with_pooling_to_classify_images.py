'''
Instructions
- Compile this model to use the categorical cross-entropy loss function and the Adam optimizer.
- Train the model for 3 epochs with batches of size 10.
- Use 20% of the data as validation data.
- Evaluate the model on test_data with test_labels (also batches of size 10).
'''

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit to training data
model.fit(train_data, train_labels, validation_split=0.2, epochs=3, batch_size=10)

# Evaluate on test data 
model.evaluate(test_data, test_labels, batch_size=10)
