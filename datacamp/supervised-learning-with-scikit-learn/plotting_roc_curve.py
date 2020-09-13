'''
Instructions
- Import roc_curve from sklearn.metrics.
- Using the logreg classifier, which has been fit to the training data, compute the predicted 
probabilities of the labels of the test set X_test. Save the result as y_pred_prob.
- Use the roc_curve() function with y_test and y_pred_prob and unpack the result into the variables fpr, tpr, and thresholds.
- Plot the ROC curve with fpr on the x-axis and tpr on the y-axis.
'''

# Import necessary modules
from sklearn.metrics import roc_curve

# Compute predicted probabilities: y_pred_prob
y_pred_prob = logreg.predict_proba(X_test)[:,1]

# Generate ROC curve values: fpr, tpr, thresholds
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Plot ROC curve
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()