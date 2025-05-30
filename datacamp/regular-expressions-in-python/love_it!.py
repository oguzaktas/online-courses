'''
Instructions
- Complete the regular expression to capture the words love or like or enjoy. 
Match and capture the words movie or concert. Match and capture anything appearing until the ..
- Find all matches of the regex in each element of sentiment_analysis. Assign them to positive_matches.
- Complete the .format() method to print out the results contained in positive_matches for each element in sentiment_analysis.
'''

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))

'''
Positive comments found [('love', 'concert', 'The Book of Souls World Tour')]
Positive comments found [('enjoy', 'movie', 'Wreck-It Ralph')]
Positive comments found [('like', 'movie', 'Wish Upon a Star')]
'''