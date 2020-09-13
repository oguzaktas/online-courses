'''
Instructions
- Fit the model to the training data (train_data).
- Use a validation split of 20%, 3 epochs and batch size of 10.
- Plot the training loss.
- Plot the validation loss.
'''

import matplotlib.pyplot as plt

# Train the model and store the training object
training = model.fit(train_data, train_labels, epochs=3, validation_split=0.2, batch_size=10)

# Extract the history from the training object
history = training.history

# Plot the training loss 
plt.plot(history['loss'])
# Plot the validation loss
plt.plot(history['val_loss'])

# Show the figure
plt.show()
