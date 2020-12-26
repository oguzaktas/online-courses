'''
Instructions
- Loop over the indices of a string using the provided len_string variable.
- Find which character will correspond to the index when we perform the shift.
- Create a generator that shifts the string 'DataCamp' by 3 positions to the right (i.e. "ampDataC").
- Create a new string using the generator and print it out.
'''

def shift_string(string, shift):
    len_string = len(string)
    # Loop over the indices of a string
    for idx in range(0, len_string):
        # Find which character will correspond to the index.
        yield string[idx - shift % len_string]
       
# Create a generator
gen = shift_string('DataCamp', 3)

# Create a new string using the generator and print it out
string_shifted = ''.join(gen)
print(string_shifted)