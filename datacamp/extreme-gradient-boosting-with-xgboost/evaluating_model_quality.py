# Create the DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary: params
params = {"objective":"reg:linear", "max_depth":4}

# Perform cross-validation: cv_results
cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=4, num_boost_round=5, metrics="rmse", as_pandas=True, seed=123)

# Print cv_results
print(cv_results)

# Extract and print final boosting round metric
print((cv_results["test-rmse-mean"]).tail(1))

# Create the DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary: params
params = {"objective":"reg:linear", "max_depth":4}

# Perform cross-validation: cv_results
cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=4, num_boost_round=5, metrics="mae", as_pandas=True, seed=123)

# Print cv_results
print(cv_results)

# Extract and print final boosting round metric
print((cv_results["test-mae-mean"]).tail(1))

'''
Output:
       train-rmse-mean  train-rmse-std  test-rmse-mean  test-rmse-std
    0    141767.539062      429.455669   142980.429688    1193.794436
    1    102832.544922      322.474657   104891.394532    1223.154574
    2     75872.617187      266.469946    79478.935547    1601.344218
    3     57245.649414      273.626175    62411.919922    2220.151196
    4     44401.295899      316.422824    51348.280274    2963.379319
    4    51348.280274
    Name: test-rmse-mean, dtype: float64

   train-mae-mean  train-mae-std  test-mae-mean  test-mae-std
0   127343.480468     668.337982  127633.976562   2403.999466
1    89770.056640     456.961189   90122.501953   2107.910394
2    63580.790039     263.409758   64278.561524   1887.567869
3    45633.153321     151.884551   46819.167969   1459.819091
4    33587.092774      86.999100   35670.645508   1140.606558
4    35670.645508
Name: test-mae-mean, dtype: float64
'''