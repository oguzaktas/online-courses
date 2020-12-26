'''
Instructions
- Convert each part marked by a red arrow to a list.
- Convert each part marked by a green arrow to a list.
- Convert each part marked by a blue arrow to a list.
- Convert each part marked by a magenta arrow to a list.
'''

spiral = []

for i in range(0, size):
    # Convert each part marked by a red arrow to a list
    spiral += list(square[i, i:size-i])
    # Convert each part marked by a green arrow to a list
    spiral += list(square[i+1:size-i, size-i-1])
    # Convert each part marked by a blue arrow to a list
    spiral += list(reversed(square[size-i-1, i:size-i-1]))
    # Convert each part marked by a magenta arrow to a list
    spiral += list(reversed(square[i+1:size-i-1, i]))
        
print(spiral)