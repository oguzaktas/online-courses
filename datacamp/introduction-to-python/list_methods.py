'''
Instructions
- Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
- Call count() on areas to find out how many times 14.5 appears in the list. Again, simply print out this number.
- Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
- Print out areas
- Use the reverse() method to reverse the order of the elements in areas.
- Print out areas once more.
'''

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
