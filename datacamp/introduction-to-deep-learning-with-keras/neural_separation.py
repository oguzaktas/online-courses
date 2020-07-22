'''
Instructions
- Use the previously defined inp_to_out() function to get the outputs of the first layer when fed with X_test.
- Use the model.evaluate() method to obtain the validation accuracy for the test dataset at each epoch.
'''

for i in range(0, 21):
  	# Train model for 1 epoch
    h = model.fit(X_train, y_train, batch_size=16, epochs=1,verbose=0)
    if i%4==0: 
      # Get the output of the first layer
      layer_output = inp_to_out([X_test])[0]
      
      # Evaluate model accuracy for this epoch
      test_accuracy = model.evaluate(X_test, y_test)[1] 
      
      # Plot 1st vs 2nd neuron output
      plot()

'''
Outputs;
In [1]: print(inspect.getsource(plot))
def plot():
  fig, ax = plt.subplots()
  plt.scatter(layer_output[:, 0], layer_output[:, 1],c=y_test,edgecolors='none')
  plt.title('Epoch: {}, Test Acc: {:3.1f} %'.format(i+1, test_accuracy * 100.0))
  plt.show()

 32/275 [==>...........................] - ETA: 0s
275/275 [==============================] - 0s 78us/step

 32/275 [==>...........................] - ETA: 0s
275/275 [==============================] - 0s 19us/step

 32/275 [==>...........................] - ETA: 0s
275/275 [==============================] - 0s 19us/step

 32/275 [==>...........................] - ETA: 0s
275/275 [==============================] - 0s 18us/step

 32/275 [==>...........................] - ETA: 0s
275/275 [==============================] - 0s 19us/step

 32/275 [==>...........................] - ETA: 0s
275/275 [==============================] - 0s 19us/step
'''