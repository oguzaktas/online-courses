# Create your housing DMatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary
params = {"objective": "reg:linear", "max_depth": 3}

# Create list of hyperparameter values: colsample_bytree_vals
colsample_bytree_vals = [0.1, 0.5, 0.8]
best_rmse = []

# Systematically vary the hyperparameter value
for curr_val in colsample_bytree_vals:
    params["colsample_bytree"] = curr_val

    # Perform cross-validation
    cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=2,
                        num_boost_round=10, early_stopping_rounds=5,
                        metrics="rmse", as_pandas=True, seed=123)

    # Append the final round rmse to best_rmse
    best_rmse.append(cv_results["test-rmse-mean"].tail().values[-1])

# Print the resultant DataFrame
print(pd.DataFrame(list(zip(colsample_bytree_vals, best_rmse)), columns=["colsample_bytree", "best_rmse"]))

'''
Output:
   colsample_bytree  best_rmse
0               0.1  50033.735
1               0.5  35656.186
2               0.8  36399.002
'''