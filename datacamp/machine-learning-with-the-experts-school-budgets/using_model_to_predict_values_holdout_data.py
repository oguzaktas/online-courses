'''
Instructions
- Read HoldoutData.csv into a DataFrame called holdout. Specify the keyword argument index_col=0 in your call to read_csv().
- Generate predictions using .predict_proba() on the numeric columns (available in the NUMERIC_COLUMNS list) of holdout. 
Make sure to fill in missing values with -1000!
'''

# Import classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Instantiate the classifier: clf
clf = OneVsRestClassifier(LogisticRegression())

# Fit it to the training data
clf.fit(X_train, y_train)

# Load the holdout data: holdout
holdout = pd.read_csv('HoldoutData.csv', index_col=0)

# Generate predictions: predictions
predictions = clf.predict_proba(holdout[NUMERIC_COLUMNS].fillna(-1000))
