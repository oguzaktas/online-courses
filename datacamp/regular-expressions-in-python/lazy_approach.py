'''
Instructions
- Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
- Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
'''

# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)