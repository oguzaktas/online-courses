'''
Instructions
- Using the compute_log_loss() function, compute the log loss for the following predicted values 
(in each case, the actual values are contained in actual_labels):
    - correct_confident.
    - correct_not_confident.
    - wrong_not_confident.
    - wrong_confident.
    - actual_labels.
'''

# Compute and print log loss for 1st case
correct_confident_loss = compute_log_loss(predicted=correct_confident, actual=actual_labels)
print("Log loss, correct and confident: {}".format(correct_confident_loss)) 

# Compute log loss for 2nd case
correct_not_confident_loss = compute_log_loss(correct_not_confident, actual_labels)
print("Log loss, correct and not confident: {}".format(correct_not_confident_loss)) 

# Compute and print log loss for 3rd case
wrong_not_confident_loss = compute_log_loss(wrong_not_confident, actual_labels)
print("Log loss, wrong and not confident: {}".format(wrong_not_confident_loss)) 

# Compute and print log loss for 4th case
wrong_confident_loss = compute_log_loss(wrong_confident, actual_labels)
print("Log loss, wrong and confident: {}".format(wrong_confident_loss)) 

# Compute and print log loss for actual labels
actual_labels_loss = compute_log_loss(actual_labels, actual_labels)
print("Log loss, actual labels: {}".format(actual_labels_loss)) 
