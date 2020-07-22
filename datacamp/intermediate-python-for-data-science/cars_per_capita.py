'''
Instructions - 1
- Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
- Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's 
True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
- Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
- Print out car_maniac to see if you got it right.

Instructions - 2
- Use the code sample above to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
- Print out medium.
'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

import numpy as np

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]

# Print medium
print(medium)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)
