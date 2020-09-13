'''
Instructions
- Import Imputer from sklearn.preprocessing.
- Create training and test sets by selecting the correct subset of sample_df: 'numeric' and 'with_missing'.
- Add the tuple ('imp', Imputer()) to the correct position in the pipeline. Pipeline processes steps sequentially, 
so the imputation step should come before the classifier step.
- Complete the .fit() and .score() methods to fit the pipeline to the data and compute the accuracy.
'''

# Import the Imputer object
from sklearn.preprocessing import Imputer

from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Create training and test sets using only numeric data
X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing']],
                                                    pd.get_dummies(sample_df['label']), 
                                                    random_state=456)

# Insantiate Pipeline object: pl
pl = Pipeline([
        ('imp', Imputer()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

# Fit the pipeline to the training data
pl.fit(X_train, y_train)

# Compute and print accuracy
accuracy = pl.score(X_test, y_test)
print("\nAccuracy on sample data - all numeric, incl nans: ", accuracy)
