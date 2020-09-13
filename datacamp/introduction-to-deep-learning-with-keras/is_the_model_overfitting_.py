'''
Instructions
- Train your model for 60 epochs, using X_test and y_test as validation data.
- Use plot_loss() passing loss and val_loss as extracted from the history attribute of the history object.
'''

# Train your model for 60 epochs, using X_test and y_test as validation data
history = model.fit(X_train, y_train, epochs=60, validation_data=(X_test, y_test), verbose=0)

# Extract from the history object loss and val_loss to plot the learning curve
plot_loss(history.history['loss'], history.history['val_loss'])

'''
Outputs;
In [1]: print(inspect.getsource(plot_loss))
def plot_loss(loss,val_loss):
  plt.figure()
  plt.plot(loss)
  plt.plot(val_loss)
  plt.title('Model loss')
  plt.ylabel('Loss')
  plt.xlabel('Epoch')
  plt.legend(['Train', 'Test'], loc='upper right')
  plt.show()
'''