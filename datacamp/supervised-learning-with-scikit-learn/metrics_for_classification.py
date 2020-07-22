'''
Instructions
- Import classification_report and confusion_matrix from sklearn.metrics.
- Create training and testing sets with 40% of the data used for testing. Use a random state of 42.
- Instantiate a k-NN classifier with 6 neighbors, fit it to the training data, and predict the labels of the test set.
- Compute and print the confusion matrix and classification report using the confusion_matrix() and classification_report() functions.
'''

# Import necessary modules
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
