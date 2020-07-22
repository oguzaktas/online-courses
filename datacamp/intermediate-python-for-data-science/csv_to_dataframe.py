'''
Instructions - 1
- To import CSV files you still need the pandas package: import it as pd.
- Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe as cars.
- Print out cars. Does everything look OK?

Instructions - 2
- Run the code with Submit Answer and assert that the first column should actually be used as row labels.
- Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
- Has the printout of cars improved now?
'''

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)
