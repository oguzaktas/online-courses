'''
Instructions
- Define a pattern to search for valid temperatures in text.
- Create an object storing the matches using finditer().
- Loop over matches_storage and print out item properties: the matching sequence, its start and end index.
'''

# Define a pattern to search for valid temperatures in text
pattern = re.compile(r'[+]?[-]{0,1}[0-9]+\.{0,1}[0-9]*\s[CF]') # re.compile(r'[+-]?\d+\.?\d* [CF]')

# Print the temperatures out
print(re.findall(pattern, text))

# Create an object storing the matches using 'finditer()'
matches_storage = re.finditer(pattern, text)

# Loop over matches_storage and print out item properties
for match in matches_storage:
    print('matching sequence = ' + match.group())
    print('start index = ' + str(match.start()))
    print('end index = ' + str(match.end()))

'''
Output:
['+23 C', '0 C', '-20.0 C', '-2.2 C', '-5.65 C', '0.0001 C', '+73.4 F', '32 F', '-4.0 F', '+28.04 F', '21.83 F', '+32.00018 F']
matching sequence = +23 C
start index = 67
end index = 72
matching sequence = 0 C
start index = 74
end index = 77
matching sequence = -20.0 C
start index = 79
end index = 86
matching sequence = -2.2 C
start index = 88
end index = 94
matching sequence = -5.65 C
start index = 96
end index = 103
matching sequence = 0.0001 C
start index = 105
end index = 113
matching sequence = +73.4 F
start index = 295
end index = 302
matching sequence = 32 F
start index = 304
end index = 308
matching sequence = -4.0 F
start index = 310
end index = 316
matching sequence = +28.04 F
start index = 318
end index = 326
matching sequence = 21.83 F
start index = 328
end index = 335
matching sequence = +32.00018 F
start index = 337
end index = 348
'''