'''
Instructions
- Split the text into an array of words using .split().
- Make lines of 4 words each, moving one word at a time.
- Instantiate a Tokenizer(), then fit it on the lines with .fit_on_texts().
- Turn lines into a sequence of numbers calling .texts_to_sequences().
'''

# Split text into an array of words 
words = text.split()

# Make lines of 4 words each, moving one word at a time
lines = []
for i in range(4, len(words)):
  lines.append(' '.join(words[i-4:i]))

# Instantiate a Tokenizer, then fit it on the lines
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)

# Turn lines into a sequence of numbers
sequences = tokenizer.texts_to_sequences(lines)
print("Lines: \n {} \n Sequences: \n {}".format(lines[:5],sequences[:5]))

'''
Outputs;
You're working with this small chunk of The Lord of The Ring quotes:
====================================================================
 It is not the strength of the body but the strength of the spirit. 
 It is useless to meet revenge with revenge it will heal nothing. 
 Even the smallest person can change the course of history.
 All we have to decide is what to do with the time that is given us. 
 The burned hand teaches best. After that, advice about fire goes to the heart.

 Lines: 
 ['it is not the', 'is not the strength', 'not the strength of', 'the strength of the', 'strength of the body'] 
 Sequences: 
 [[5, 2, 42, 1], [2, 42, 1, 6], [42, 1, 6, 4], [1, 6, 4, 1], [6, 4, 1, 10]]
 '''