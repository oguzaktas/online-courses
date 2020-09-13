'''
Instructions
- Find the index where money occurs between characters with index 12 and 50. If not found, the method should return -1.
- Find the index where money occurs between characters with index 12 and 50. If not found, it should raise an error.
'''

for movie in movies:
  # Find the first occurrence of word
  print(movie.find("money", 12, 51))

for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index("money", 12, 51))
  except ValueError:
    print("substring not found")