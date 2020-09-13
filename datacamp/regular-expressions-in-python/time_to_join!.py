'''
Instructions
- Remove tag <\i> from the end of the string. Print the results.
- Split the string contained in movie_tag using the commas as a separating element. Print the results.
- Join back together the list of substring contained in movie_no_comma using whitespace as join elements. Print the results.
'''

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = " ".join(movie_no_comma)
print(movie_join)