'''
Instructions - 1
- Create a for loop to loop over flash and print the values in the list. Use person as the loop variable.
- Create an iterator for the list flash and assign the result to superspeed.
- Print each of the items from superspeed using next() 4 times.

Instructions - 2
- Create an iterator object small_value over range(3) using the function iter().
- Using a for loop, iterate over range(3), printing the value for every iteration. Use num as the loop variable.
- Create an iterator object googol over range(10 ** 100).
'''

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for name in flash:
    print(name)

# Create an iterator for flash: superspeed
superspeed = iter(flash)

# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
