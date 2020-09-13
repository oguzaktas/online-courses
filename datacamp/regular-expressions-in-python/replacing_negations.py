'''
Instructions
- Replace the substring isn't for the word is.
- Replace the substring important for the word insignificant.
- Print out the result contained in the variable movies_antonym.
'''

# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)

'''
Output:
<script.py> output:
    the rest of the story is insignificant because all it does is serve as a mere backdrop for the two stars to share the screen .
'''