'''
Instructions
- Import the re module.
- Write a regex that matches the user mentions that follows the pattern, e.g. @robot3!.
- Find all the matches of the pattern in the sentiment_analysis variable.
'''

# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

'''
<script.py> output:
    ['@robot9!', '@robot4&', '@robot9$', '@robot7%']
'''