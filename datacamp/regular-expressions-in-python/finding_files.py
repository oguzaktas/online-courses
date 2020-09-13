'''
Instructions
- Write a regex that matches the pattern of the text file names, e.g. aemyfile.txt.
- Find all matches of the regex in the elements of sentiment_analysis. Print out the result.
- Replace all matches of the regex with an empty string "". Print out the result.
'''

# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}\w+.txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))
    
	# Replace all matches with empty string
	print(re.sub(regex, "", text))