'''
Instructions
- Import LogisticRegression from sklearn.linear_model and OneVsRestClassifier from sklearn.multiclass.
- Instantiate the classifier clf by placing LogisticRegression() inside OneVsRestClassifier().
- Fit the classifier to the training data X_train and y_train.
- Compute and print the accuracy of the classifier using its .score() method, which accepts two arguments: X_test and y_test.
'''

# Import classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Create the DataFrame: numeric_data_only
numeric_data_only = df[NUMERIC_COLUMNS].fillna(-1000)

# Get labels and convert to dummy variables: label_dummies
label_dummies = pd.get_dummies(df[LABELS])

# Create training and test sets
X_train, X_test, y_train, y_test = multilabel_train_test_split(numeric_data_only,
                                                               label_dummies,
                                                               size=0.2, 
                                                               seed=123)

# Instantiate the classifier: clf
clf = OneVsRestClassifier(LogisticRegression())

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Print the accuracy
print("Accuracy: {}".format(clf.score(X_test, y_test)))
