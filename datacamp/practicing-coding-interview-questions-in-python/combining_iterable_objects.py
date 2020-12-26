'''
Instructions
- Define a function searching for the longest word given a list of words.
- Create a list of the lengths of each list in wlist.
- Create a list of the longest words in each list in wlist.
- Combine wlist, lengths, and words into one iterable object and print each element.
'''

# Define a function searching for the longest word
def get_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Create a list of the lengths of each list in wlist
lengths = [len(item) for item in wlist]

# Create a list of the longest words in each list in wlist
words = [get_longest_word(item) for item in wlist]

# Combine the resulting data into one iterable object
for item in zip(wlist, lengths, words):
    print(item)