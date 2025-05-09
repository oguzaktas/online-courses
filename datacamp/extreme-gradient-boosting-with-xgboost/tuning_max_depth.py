# Create your housing DMatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary
params = {"objective": "reg:linear"}

# Create list of max_depth values
max_depths = [2, 5, 10, 20]
best_rmse = []

# Systematically vary the max_depth
for curr_val in max_depths:
    params["max_depth"] = curr_val

    # Perform cross-validation
    cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=2, metrics="rmse",
                        num_boost_round=10, as_pandas=True, seed=123, early_stopping_rounds=5)

    # Append the final round rmse to best_rmse
    best_rmse.append(cv_results["test-rmse-mean"].tail().values[-1])

# Print the resultant DataFrame
print(pd.DataFrame(list(zip(max_depths, best_rmse)), columns=["max_depth", "best_rmse"]))

'''
Output:
   max_depth  best_rmse
0          2  37957.469
1          5  35596.600
2         10  36065.547
3         20  36739.576
'''