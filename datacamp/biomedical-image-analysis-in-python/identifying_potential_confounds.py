'''
Instructions
- Print three random rows in df using the .sample() method.
- Print the unique number of individuals with Alzheimer's disease patients.
- Print the correlation table between each variable.
'''

# Print random sample of rows
print(df.sample(3))

# Print prevalence of Alzheimer's Disease
print(df.alzheimers.value_counts())

# Print a correlation table
print(df.corr())
