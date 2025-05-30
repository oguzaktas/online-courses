'''
Instructions
- Create a KNN model with default hyperparameters.
- Fit the model.
- Print out the prediction for the test example 0.
'''

from sklearn.neighbors import KNeighborsClassifier

# Create and fit the model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Predict on the test features, print the results
pred = knn.predict(X_test)[0]
print("Prediction for test example 0:", pred)