'''
Instructions
- Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago.
- Complete the for-loop with a regex that finds all dates in a format similar to 23rd june 2018.
- Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25.
'''

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\w+\sago", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w{2}\s\w+\s\d{4}", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w{2}\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))