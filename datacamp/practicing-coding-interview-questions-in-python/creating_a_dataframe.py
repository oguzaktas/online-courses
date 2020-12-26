'''
Instructions
- Create a list with tuples of the form (word itself, length of the word).
- Unwrap the word_lengths and create two separate tuples words and lengths.
- Create a zip object combining column names for the future DataFrame and the associated data.
- Convert result to a dictionary and build a DataFrame.
'''

# Create a list of tuples with words and their lengths
word_lengths = [
    (item, len(item)) for items in wlist for item in items
]

# Unwrap the word_lengths
words, lengths = zip(*word_lengths)

# Create a zip object
col_names = ['word', 'length']
result = zip(col_names, [words, lengths])

# Convert the result to a dictionary and build a DataFrame
data_frame = pd.DataFrame(dict(result))
print(data_frame)