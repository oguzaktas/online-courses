'''
Instructions
- Set up a pipeline with the following steps:
    - 'imputation', which uses the Imputer() transformer and the 'mean' strategy to impute missing data ('NaN') using the mean of the column.
    - 'scaler', which scales the features using StandardScaler().
    - 'elasticnet', which instantiates an ElasticNet() regressor.
- Specify the hyperparameter space for the l1 ratio using the following notation: 'step_name__parameter_name'. 
Here, the step_name is elasticnet, and the parameter_name is l1_ratio.
- Create training and test sets, with 40% of the data used for the test set. Use a random state of 42.
- Instantiate GridSearchCV with the pipeline and hyperparameter space. Use 3-fold cross-validation (This is the default, so you don't have to specify it).
- Fit the GridSearchCV object to the training set.
- Compute R2 and the best parameters. This has been done for you, so hit 'Submit Answer' to see the results!
'''

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import Imputer
from sklearn.linear_model import ElasticNet

# Setup the pipeline steps: steps
steps = [('imputation', Imputer(missing_values='NaN', strategy='mean', axis=0)),
         ('scaler', StandardScaler()),
         ('elasticnet', ElasticNet())]

# Create the pipeline: pipeline 
pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'elasticnet__l1_ratio':np.linspace(0,1,30)}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Create the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(pipeline, param_grid=parameters)

# Fit to the training set
gm_cv.fit(X_train, y_train)

# Compute and print the metrics
r2 = gm_cv.score(X_test, y_test)
print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))
