'''
Instructions
- Write a regex that matches the number of user mentions given as, for example, User_mentions:9 in sentiment_analysis.
- Write a regex that matches the number of likes given as, for example, likes: 5 in sentiment_analysis.
- Write a regex that matches the number of retweets given as, for example, number of retweets: 4 in sentiment_analysis.
'''

# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))

# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))