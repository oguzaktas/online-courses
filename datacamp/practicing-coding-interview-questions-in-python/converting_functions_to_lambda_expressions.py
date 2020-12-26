'''
Instructions
- Convert func1() to a lambda expression.
- Convert func2() to a lambda expression.
- Convert func3() to a lambda expression.
'''

# Convert func1() to a lambda expression
lambda1 = lambda x, y: x if x >= y else y
print(str(func1(5, 4)) + ', ' + str(lambda1(5, 4)))
print(str(func1(4, 5)) + ', ' + str(lambda1(4, 5)))

# Convert func2() to a lambda expression
lambda2 = lambda s: dict((c, s.count(c)) for c in set(s))

# Convert func3() to a lambda expression
lambda3 = lambda *nums: math.sqrt(sum(n**2 for n in nums))
print(str(func3(3, 4)) + ', ' + str(lambda3(3, 4)))
print(str(func3(3, 4, 5)) + ', ' + str(lambda3(3, 4, 5)))