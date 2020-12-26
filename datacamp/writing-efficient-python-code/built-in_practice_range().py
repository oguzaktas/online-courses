'''
Instructions
- Create a range object that starts at zero and ends at five. Only use a stop argument.
- Convert the nums variable into a list called nums_list.
- Create a new list called nums_list2 that starts at one, ends at eleven, 
and increments by two by unpacking a range object using the star character (*).
'''

# Create a range object that goes from 0 to 5
nums = range(0, 6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)