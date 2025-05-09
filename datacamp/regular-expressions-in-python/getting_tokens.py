'''
Instructions
- Write a regex that matches the described hashtag pattern. Assign it to the regex variable.
- Replace all the matches of the regex with an empty string "". Assign it to no_hashtag variable.
- Split the text in the no_hashtag variable at every match of one or more consecutive whitespace.
'''

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))