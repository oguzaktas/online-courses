'''
Instructions
- Split the string file into many substrings at line boundaries.
- Print out the resulting variable file_split.
- Complete the for-loop to split the strings into many substrings using commas as a separator element.
'''

# Split string at line boundaries
file_split = file.split("\n")

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(sep=",")
    print(substring_split)

'''
Output:
<script.py> output:
    ['mtv films election, a high school comedy, is a current example', 'from there, director steven spielberg wastes no time, taking us into the water on a midnight swim']
    ['mtv films election', ' a high school comedy', ' is a current example']
    ['from there', ' director steven spielberg wastes no time', ' taking us into the water on a midnight swim']
'''