'''
Instructions
- Compile the network using the 'adam' optimizer and the 'categorical_crossentropy' 
cost function. In the metrics list define that the network to report 'accuracy'.
- Fit the network on train_data and train_labels. Train for 3 epochs with a batch size of 10 images. 
In training, set aside 20% of the data as a validation set, using the validation_split keyword argument.
'''

# Compile the model 
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Fit the model on a training set
model.fit(train_data, train_labels, 
          validation_split=0.2, 
          epochs=3, batch_size=10)

# Evaluate the model on separate test data
model.evaluate(test_data, test_labels, batch_size=10)
