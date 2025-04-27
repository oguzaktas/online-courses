'''
Instructions
- Import Ridge from sklearn.linear_model and cross_val_score from sklearn.model_selection.
- Instantiate a ridge regressor called ridge with alpha=0.5 and normalize=True.
- Perform 5-fold cross-validation on X and y using the cross_val_score() function.
- Print the cross-validated scores.
'''

# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X, y, cv=5)

# Print the cross-validated scores
print(ridge_cv)
