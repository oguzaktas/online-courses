'''
Instructions
- Find out how many characters the variable movie has.
- Convert the numeric variable length_string to a string representation.
- Concatenate the predefined variable statement and the variable to_string adding a space between them. Print out the result.
'''

# Find characters in movie variable
length_string = len(movie)

# Convert to string
to_string = str(length_string)

# Predefined variable
statement = "Number of characters in this review:"

# Concatenate strings and print result
print(statement + " " + to_string)