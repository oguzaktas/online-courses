'''
Instructions
- Define the lambda function categorize_label to convert column x into x.astype('category').
- Use the LABELS list provided to convert the subset of data df[LABELS] to categorical types 
using the .apply() method and categorize_label. Don't forget axis=0.
- Print the converted .dtypes attribute of df[LABELS].
'''

import pandas as pd

# Define the lambda function: categorize_label
categorize_label = lambda x: x.astype('category')

# Convert df[LABELS] to a categorical type
df[LABELS] = df[LABELS].apply(categorize_label, axis=0)

# Print the converted dtypes
print(df[LABELS].dtypes)
