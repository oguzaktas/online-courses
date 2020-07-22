'''
Instructions
- Loop over the different values of C_value, creating and fitting a LogisticRegression model each time.
- Save the error on the training set and the validation set for each model.
- Create a plot of the training and testing error as a function of the regularization parameter, C.
- Looking at the plot, what's the best value of C?
'''

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Train and validaton errors initialized as empty list
train_errs = list()
valid_errs = list()

# Loop over values of C_value
for C_value in [0.001, 0.01, 0.1, 1, 10, 100, 1000]:
    # Create LogisticRegression object and fit
    lr = LogisticRegression(C=C_value)
    lr.fit(X_train, y_train)
    
    # Evaluate error rates and append to lists
    train_errs.append( 1.0 - lr.score(X_train, y_train) )
    valid_errs.append( 1.0 - lr.score(X_valid, y_valid) )
    
# Plot results
plt.semilogx(C_values, train_errs, C_values, valid_errs)
plt.legend(("train", "validation"))
plt.show()
