'''
Instructions - 1
- In the function read_large_file(), read a line from file_object by using the method readline(). Assign the result to data.
- In the function read_large_file(), yield the line read from the file data.
- In the context manager, create a generator object gen_file by calling your generator function read_large_file() and passing file to it.
- Print the first three lines produced by the generator object gen_file using next().

Instructions - 2
- Bind the file 'world_dev_ind.csv' to file in the context manager with open().
- Complete the for loop so that it iterates over the generator from the call to read_large_file() to process all the rows of the file.
'''

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)
