'''
Instructions - 1
- Use member as the iterator variable in the list comprehension. For the conditional, use len() to evaluate 
the iterator variable. Note that you only want strings with 7 characters or more.

Instructions - 2
- In the output expression, keep the string as-is if the number of characters is >= 7, else replace it with an empty string - that is, '' or "".
'''

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else member.replace(member, '') for member in fellowship]

# Print the new list
print(new_fellowship)
