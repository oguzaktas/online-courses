'''
Instructions
- Convert the string in the variable movie to lowercase. Print the result.
- Remove the $ that occur at the start and at the end of the string contained in movie_lower. Print the results.
- Split the string contained in movie_no_space into as many substrings as possible. Print the results.
- To get the root of the second word contained in movie_split, select all the characters except the last one.
'''

# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove whitespaces and print the result
movie_no_space = movie_lower.strip("$")
print(movie_no_space)

# Split the string into substrings and print the result
movie_split = movie_no_space.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][0]
print(word_root)