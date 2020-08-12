'''
Instructions - 1
- Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JAP, 
the index is 2. Make sure to print the resulting Series.
- Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes 
of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.

Instructions - 2
- Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
- Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.

Instructions - 3
- Print out the drives_right column as a Series using loc or iloc.
- Print out the drives_right column as a DataFrame using loc or iloc.
- Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.
'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JAP'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
