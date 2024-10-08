'''
Instructions
- Modify the function header such that the function name is now shout_all, and it accepts two parameters, word1 and word2, in that order.
- Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2, respectively.
- Construct a tuple shout_words, composed of shout1 and shout2.
- Call shout_all() with the strings 'congratulations' and 'you' and assign the result to yell1 and yell2.
'''

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)
