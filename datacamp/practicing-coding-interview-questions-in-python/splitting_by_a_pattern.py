'''
Instructions
- Compile a regular expression that splits strings in movies into a movie name and its director.
- Retrieve a movie name and its director using re.split().
- Create a new string with a movie name and its director separated by ,.
- Append the resulting string to movies_without_year.
'''

# Compile a regular expression
pattern = re.compile(r', \d+, ')

movies_without_year = []
for movie in movies:
    # Retrieve a movie name and its director
    split_result = re.split(pattern, movie)
    # Create a new string with a movie name and its director
    movie_and_director = ', '.join(split_result)
    # Append the resulting string to movies_without_year
    movies_without_year.append(movie_and_director)
    
for movie in movies_without_year:
    print(movie)