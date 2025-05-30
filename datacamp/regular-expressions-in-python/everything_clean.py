'''
Instructions
- Import the re module.
- Write a regex to find all the matches of http links appearing in each tweet in sentiment_analysis. Print out the result.
- Write a regex to find all the matches of user mentions appearing in each tweet in sentiment_analysis. Print out the result.
'''

# Import re module
import re

for tweet in sentiment_analysis:
	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))

'''
<script.py> output:
    ['https://www.tellyourstory.com']
    ['@blueKnight39']
    []
    ['@anitaLopez98', '@MyredHat31']
    ['https://radio.foxnews.com']
    ['@YourBestCompany', '@foxRadio']
'''