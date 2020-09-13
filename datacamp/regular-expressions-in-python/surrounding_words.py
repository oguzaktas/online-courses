'''
Instructions
- Get all the words that are followed by the word python in sentiment_analysis. Print out the word found.
- Get all the words that are preceded by the word python or Python in sentiment_analysis. Print out the words found.
'''

# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Positive lookbehind
look_behind = re.findall(r"(?<=[pP]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)