'''
Instructions
- Complete the regular expression to capture the words hate or dislike or disapprove. 
Match but don't capture the words movie or concert. Match and capture anything appearing until the ..
- Find all matches of the regex in each element of sentiment_analysis. Assign them to negative_matches.
- Complete the .format() method to print out the results contained in negative_matches for each element in sentiment_analysis.
'''

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))

'''
<script.py> output:
    Negative comments found [('dislike', 'The cabin and the ant')]
    Negative comments found [('disapprove', 'Honest with you')]
    Negative comments found [('dislike', 'After twelve Tour')]
'''