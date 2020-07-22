'''
Instructions - 1
- Use single square brackets to print out the country column of cars as a Pandas Series.
- Use double square brackets to print out the country column of cars as a Pandas DataFrame.
- Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order.

Instructions - 2
- Select the first 3 observations from cars and print them out.
- Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.
'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
