'''
Instructions
- Complete the regular expression to match an elongated word as described.
- Search the elements in sentiment_analysis list to find out if they contain elongated words. Assign the result to match_elongated.
- Assign the captured group number zero to the variable elongated_word.
- Print the result contained in the variable elongated_word.
'''

# Complete the regex to match an elongated word
regex_elongated = r"\w+(\w)\1\w*"

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
	match_elongated = re.search(regex_elongated, tweet)
    
	if match_elongated:
		# Assign the captured group zero 
		elongated_word = match_elongated.group(0)
        
		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found") 

'''
<script.py> output:
    Elongated word found: Moscooooooow
    Elongated word found: neighborrrrrrrs
    No elongated word found
'''