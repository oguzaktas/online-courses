'''
Instructions
- Compute the maximum predicted probability.
- Run the provided code and take a look at the plot.
'''

from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression

# Set the regularization strength
model = LogisticRegression(C=1)

# Fit and plot
model.fit(X,y)
plot_classifier(X,y,model,proba=True)

# Predict probabilities on training points
prob = model.predict_proba(X)
print("Maximum predicted probability", np.max(prob))
