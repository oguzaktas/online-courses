'''
Instructions
- Evaluate the small model using the train data.
- Evaluate the small model using the test data.
- Evaluate the large model using the train data.
- Evaluate the large model using the test data.
'''

# Evaluate the small model using the train data
small_train = small_model.evaluate(train_features, train_labels)

# Evaluate the small model using the test data
small_test = small_model.evaluate(test_features, test_labels)

# Evaluate the large model using the train data
large_train = large_model.evaluate(train_features, train_labels)

# Evaluate the large model using the test data
large_test = large_model.evaluate(test_features, test_labels)

# Print losses
print('\n Small - Train: {}, Test: {}'.format(small_train, small_test))
print('Large - Train: {}, Test: {}'.format(large_train, large_test))

'''
Output:
 32/100 [========>.....................] - ETA: 0s - loss: 0.2297
100/100 [==============================] - 0s 1ms/sample - loss: 0.2450

 32/100 [========>.....................] - ETA: 0s - loss: 0.4059
100/100 [==============================] - 0s 110us/sample - loss: 0.4022

 32/100 [========>.....................] - ETA: 0s - loss: 0.0409
100/100 [==============================] - 0s 2ms/sample - loss: 0.0381

 32/100 [========>.....................] - ETA: 0s - loss: 0.1521
100/100 [==============================] - 0s 83us/sample - loss: 0.1440

 Small - Train: 0.2449816483259201, Test: 0.4021979570388794
Large - Train: 0.03811386965215206, Test: 0.14401205599308015
'''