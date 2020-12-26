'''
Instructions
- Print the second row of nums.
- Print the items of nums that are greater than six.
- Create nums_dbl that doubles each number in nums.
- Replace the third column in nums with a new column that adds 1 to each item in the original column.
'''

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)