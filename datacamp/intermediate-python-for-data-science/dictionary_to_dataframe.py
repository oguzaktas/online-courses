'''
Instructions - 1
- Import pandas as pd.
- Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
    - key 'country' and value names.
    - key 'drives_right' and value dr.
    - key 'cars_per_cap' and value cpc.
- Use pd.DataFrame() to turn your dict into a DataFrame called cars.
- Print out cars and see how beautiful it is.

Instructions - 2
- Hit Submit Answer to see that, indeed, the row labels are not correctly set.
- Specify the row labels by setting cars.index equal to row_labels.
- Print out cars again and check if the row labels are correct this time.
'''

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
