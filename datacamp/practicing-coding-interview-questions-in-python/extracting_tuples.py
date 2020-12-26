'''
Instructions
- Create a list of tuples each containing the length and the longest word of each item in wlist.
- Unwrap the created list and create two distinct tuples.
'''

# Create a list of tuples with lengths and longest words
result = [
    (len(item), get_longest_word(item)) for item in wlist
]

# Unzip the result    
lengths, words = zip(*result)

for item in zip(wlist, lengths, words):
    print(item)