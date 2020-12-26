'''
Instructions
- Instead of using for i in range(len(names)), update the for loop to use i as 
the index variable and name as the iterator variable and use enumerate().
- Rewrite the previous for loop using enumerate() and list comprehension to create a new list, indexed_names_comp.
- Create another list (indexed_names_unpack) by using the star character (*) to unpack the enumerate object 
created from using enumerate() on names. This time, start the index for enumerate() at one instead of zero.
'''

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)