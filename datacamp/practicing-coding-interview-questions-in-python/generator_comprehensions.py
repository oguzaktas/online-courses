'''
Instructions
- Rewrite func1() as a generator comprehension with n = 10
- Rewrite func2() as a generator comprehension with n = 20
- Rewrite func3() as a generator comprehension with n = 8 and m = 10.
'''

# Rewrite func1() as a generator comprehension
gen = (i ** 2 for i in range(0, 10))

for item in zip(gen, func1(10)):
    print(item)

# Rewrite func2() as a generator comprehension
gen = (2 * i for i in range(0, 20) if i % 2 == 0)

for item in zip(gen, func2(20)):
    print(item)

# Rewrite func3() as a generator comprehension
gen = (((i, j), i + j) for i in func1(8) for j in func2(10))

for item in zip(gen, func3(8, 10)):
    print(item)