'''
Instructions
- Take x and return x**2 if x > 0  and 0, otherwise.
- Take a list of integers nums and leave only even numbers.
- Take strings s1, s2 and list their common characters.
'''

# Take x and return x squared if x > 0 and 0, otherwise
squared_no_negatives = lambda x: x ** 2 if x > 0 else 0
print(squared_no_negatives(2.0))
print(squared_no_negatives(-1))

# Take a list of integers nums and leave only even numbers
get_even = lambda nums: [i for i in nums if i % 2 == 0]
print(get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Take strings s1, s2 and list their common characters
common_chars =  lambda s1, s2: list(sorted(set.intersection(set(s1), set(s2))))
print(common_chars('pasta', 'pizza'))