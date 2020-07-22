'''
Instructions
- Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
- Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
- Print both downstairs and upstairs using print().
- Use slicing to create the lists downstairs and upstairs again, but this time without using indexes if it's not necessary. 
Remember downstairs is the first 6 elements of areas and upstairs is the last 4 elements of areas.
'''

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]
