'''
Instructions
- Substitute the code in the block 1 given the input_array1.
- Substitute the code in the block 2 given input_array2.
- Substitute the code in the block 3 given input_array3.
'''

# Substitute the code in the block 1 given the input_array1
output_array1 = list(map(lambda x: [5*i for i in x], input_array1))

print(list(map(lambda x: [5*i for i in x], input_list1)))
print(output_array1)

# Substitute the code in the block 2 given the input_array2
output_array2 = list(filter(lambda x: x % 2 == 0, input_array2))
print(list(filter(lambda x: x % 2 == 0, input_list2)))
print(output_array2)

# Substitute the code in the block 3 given the input_array3
output_array3 = [[i*i for i in j] for j in input_array3]
print([[i*i for i in j] for j in input_list3])
print(output_array3)