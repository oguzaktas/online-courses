'''
Instructions
- Retrieve Iterable lengths from args using map() and find the minimal length.
- Within the loop, create the mapping using map() to retrieve the elements in args with the same index i.
- Convert the mapping to a tuple and append it to the tuple_list.
'''

def my_zip(*args):
    
    # Retrieve Iterable lengths and find the minimal length
    lengths = list(map(lambda x: len(x), args))
    min_length = min(lengths)

    tuple_list = []
    for i in range(0, min_length):
        # Map the elements in args with the same index i
        mapping = map(lambda j: i + 1, args)
        # Convert the mapping and append it to tuple_list
        tuple_list.append(tuple(mapping))

    return tuple_list

result = my_zip([1, 2, 3], ['a', 'b', 'c', 'd'], 'DataCamp')
print(result)