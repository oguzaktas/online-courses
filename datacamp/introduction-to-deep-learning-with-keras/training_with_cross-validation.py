'''
Instructions
- Import KerasClassifier from keras scikit_learn wrappers.
- Create a KerasClassifier the function to create the model, the best number of epochs, and the best batch_size.
- Pass your model, features, and labels to perform cross-validation with 3 folds.
'''

# Import KerasClassifier from keras wrappers
from keras.wrappers.scikit_learn import KerasClassifier

# Create a KerasClassifier
model = KerasClassifier(build_fn = create_model, epochs = 50, 
             batch_size = 128, verbose = 0)

# Calculate the accuracy score for each fold
kfolds = cross_val_score(X, y, model, cv = 3)

# Print the mean accuracy
print('The mean accuracy was:', kfolds.mean())

# Print the accuracy standard deviation
print('With a standard deviation of:', kfolds.std())

'''
Output;

<script.py> output:
    The mean accuracy was: 0.9718834066666666
    With a standard deviation of: 0.002448915612216046
'''