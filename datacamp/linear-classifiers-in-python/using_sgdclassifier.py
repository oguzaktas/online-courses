'''
Instructions
- Instantiate an SGDClassifier instance with random_state=0.
- Search over the regularization strength, the hinge vs. log losses, and L1 vs. L2 regularization.
'''

from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV

# We set random_state=0 for reproducibility 
linear_classifier = SGDClassifier(random_state=0)

# Instantiate the GridSearchCV object and run the search
parameters = {'alpha':[0.00001, 0.0001, 0.001, 0.01, 0.1, 1], 
             'loss':['log', 'hinge'], 'penalty':['l1', 'l2']}
searcher = GridSearchCV(linear_classifier, parameters, cv=10)
searcher.fit(X_train, y_train)

# Report the best parameters and the corresponding score
print("Best CV params", searcher.best_params_)
print("Best CV accuracy", searcher.best_score_)
print("Test accuracy of best grid search hypers:", searcher.score(X_test, y_test))

'''
<script.py> output:
    Best CV params {'alpha': 0.0001, 'loss': 'hinge', 'penalty': 'l1'}
    Best CV accuracy 0.94351630867144
    Test accuracy of best grid search hypers: 0.9592592592592593
'''
