'''
Instructions
- Create a range object that would produce the values from 10 to 20 using range(). Assign the result to values.
- Use the list() function to create a list of values from the range object values. Assign the result to values_list.
- Use the sum() function to get the sum of the values from 10 to 20 from the range object values. Assign the result to values_sum.
'''

# Create a range object: values
values = range(10, 21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)
