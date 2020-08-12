'''
Instructions
- Create the following classifier objects with default hyperparameters: LogisticRegression, LinearSVC, SVC, KNeighborsClassifier.
- Fit each of the classifiers on the provided data using a for loop.
- Call the plot_4_classifers() function (similar to the code here), passing in X, y, and a list containing the four classifiers.
'''

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt

# Define the classifiers
classifiers = [LogisticRegression(), LinearSVC(), KNeighborsClassifier()]

# Fit the classifiers
for c in classifiers:
    c.fit(X, y)

# Plot the classifiers
plot_4_classifiers(X, y, classifiers)
plt.show()
