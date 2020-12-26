'''
Instructions
- Calculate the value for z coordinate using coordinates x and y.
- Create a new key for the dictionary circ_parab represented as a tuple containing x and y.
- Create a new key-value pair for circ_parab.
'''

circ_parab = dict()

for x in range_x:
    for y in range_y:        
        # Calculate the value for z
        z = (x**2) + (y**2)
        # Create a new key for the dictionary
        key = (x, y)
        # Create a new key-value pair      
        circ_parab[key] = z

'''
Output:
range_x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
range_y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
'''