'''
Instructions
- Using a combination of list subsetting and variable assignment, create a new variable, 
eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
- Print the new variable eat_sleep_area.
'''

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)
