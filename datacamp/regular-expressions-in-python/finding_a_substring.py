'''
Instructions
- Find if the substring actor occurs between the characters with index 37 and 41 inclusive. 
If it is not detected, print the statement Word not found.
- Replace actor actor with the substring actor if actor occurs only two repeated times.
- Replace actor actor actor with the substring actor if actor appears three repeated times.
'''

for movie in movies:
  	# Find if actor occurrs between 37 and 41 inclusive
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two by one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences by one
        print(movie.replace("actor actor actor", "actor"))

'''
Output:
<script.py> output:
    Word not found
    I believe you I always said that the actor is amazing in every movie he has played
    it's astonishing how frightening the actor norton looks with a shaved head and a swastika on his chest.
'''