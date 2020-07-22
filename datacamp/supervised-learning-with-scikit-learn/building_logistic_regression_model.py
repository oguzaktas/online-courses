'''
Instructions
- Import:
    - LogisticRegression from sklearn.linear_model.
    - confusion_matrix and classification_report from sklearn.metrics.
- Create training and test sets with 40% (or 0.4) of the data used for testing. Use a random state of 42. This has been done for you.
- Instantiate a LogisticRegression classifier called logreg.
- Fit the classifier to the training data and predict the labels of the test set.
- Compute and print the confusion matrix and classification report. This has been done for you, 
so hit 'Submit Answer' to see how logistic regression compares to k-NN!
'''

# Import the necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

# Create the classifier: logreg
logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = logreg.predict(X_test)

# Compute and print the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
