# Create the DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary: params
params = {"objective":"reg:linear", "max_depth":2}

# Train the model: xg_reg
xg_reg = xgb.train(params=params, dtrain=housing_dmatrix, num_boost_round=10)

# Plot the first tree
xgb.plot_tree(booster=xg_reg, num_trees=0)
plt.show()

# Plot the fifth tree
xgb.plot_tree(booster=xg_reg, num_trees=4)
plt.show()

# Plot the last tree sideways
xgb.plot_tree(booster=xg_reg, num_trees=9, rankdir="LR")
plt.show()
