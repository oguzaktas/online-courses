'''
Instructions
- Sort words by string length.
- Sort words by the last character in a string.
- Sort words by the total amount of characters a, b, and c (e.g., the word 'cabana' has 3 a's, 1 b, and 1 c; in total, 5)
'''

# Sort words by the string length
words.sort(key=lambda s: len(s))
print(words)

# Sort words by the last character in a string
words.sort(key=lambda s: s[-1])
print(words)

# Sort words by the total amount of certain characters
words.sort(key=lambda s: s.count('a') + s.count('b') + s.count('c'))
print(words)