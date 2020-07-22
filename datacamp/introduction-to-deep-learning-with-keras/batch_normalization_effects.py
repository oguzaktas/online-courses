'''
Instructions
- Train the standard_model for 10 epochs passing in train and validation data, storing its history in history1.
- Train your batchnorm_model for 10 epochs passing in train and validation data, storing its history in history2.
- Call compare_histories_acc passing in history1 and history2.
'''

# Train your standard model, storing its history
history1 = standard_model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=0)

# Train the batch normalized model you recently built, store its history
history2 = batchnorm_model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=0)

# Call compare_acc_histories passing in both model histories
compare_histories_acc(history1, history2)

'''
Outputs;
In [1]: print(inspect.getsource(compare_histories_acc))
def compare_histories_acc(h1,h2):
  plt.plot(h1.history['acc'])
  plt.plot(h1.history['val_acc'])
  plt.plot(h2.history['acc'])
  plt.plot(h2.history['val_acc'])
  plt.title("Batch Normalization Effects")
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend(['Train', 'Test', 'Train with Batch Normalization', 'Test with Batch Normalization'], loc='best')
  plt.show()
'''