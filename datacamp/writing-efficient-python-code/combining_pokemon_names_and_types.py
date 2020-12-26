'''
Instructions
- Combine the names list and the primary_types list into a new list object (called names_type1).
- Combine names, primary_types, and secondary_types (in that order) using zip() and unpack the zip object into a new list.
- Use zip() to combine the first five items from the names list and the first three items from the primary_types list.
'''

# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')