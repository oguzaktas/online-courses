'''
Instructions
- Create a GridSearchCV object.
- Call the fit() method to select the best value of gamma based on cross-validation accuracy.
'''

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# Instantiate an RBF SVM
svm = SVC()

# Instantiate the GridSearchCV object and run the search
parameters = {'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
searcher = GridSearchCV(svm, parameters)
searcher.fit(X, y)

# Report the best parameters
print("Best CV params", searcher.best_params_)
