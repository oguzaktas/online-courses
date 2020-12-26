'''
Instructions
- Create an empty list called formal_list using the formal name (list()).
- Create an empty list called literal_list using the literal syntax ([]).
- Print out the type of formal_list and literal_list to show that both naming conventions create a list.
'''

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

'''
%timeit l = list()
%timeit l = []
Output:
77.4 ns +- 1.12 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
18.8 ns +- 0.379 ns per loop (mean +- std. dev. of 7 runs, 100000000 loops each)
'''