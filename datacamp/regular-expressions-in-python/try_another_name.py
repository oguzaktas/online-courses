'''
Instructions
- Complete the regex to match the email capturing only the name part. The name part appears before the @.
- Find all matches of the regex in each element of sentiment_analysis analysis. Assign it to the variable email_matched.
- Complete the .format() method to print the results captured in each element of sentiment_analysis analysis.
'''

# Write a regex that matches email
regex_email = r"([a-zA-Z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))