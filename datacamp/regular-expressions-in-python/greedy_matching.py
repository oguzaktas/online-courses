'''
Instructions
- Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.
- Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis.
'''

# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)