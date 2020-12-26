'''
Instructions
- Convert the text to lower case and create a word list.
- Create a set that will store only unique words from the list.
- Using list comprehension, create a dictionary that counts a word appearance in the word list.
- Print words that appear in the word_counter more than once.
'''

# Convert the text to lower case and create a word list
words = create_word_list(spam.lower())

# Create a set storing only unique words
word_set = set(words)

# Create a dictionary that counts each word in the list
tuples = [(word, words.count(word)) for word in word_set]
word_counter = dict(tuples)

# Printing words that appear more than once
for (key, value) in word_counter.items():
    if value > 1:
        print("{}: {}".format(key, value))