'''
Instructions
- Multiply the arrays with each other and sum the result to find the total number of correct predictions.
- Divide the number of correct answers (the sum) by the length of predictions array to calculate the proportion of correct predictions.
'''

# Calculate the number of correct predictions
number_correct = (predictions * test_labels).sum()
print(number_correct)

# Calculate the proportion of correct predictions
proportion_correct = number_correct / len(predictions)
print(proportion_correct)
