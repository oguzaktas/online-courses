'''
Instructions - 1
- Use pd.read_csv() to read in 'ind_pop.csv' in chunks of size 10. Assign the result to df_reader.
- Print the first two chunks from df_reader.

Instructions - 2
- Use pd.read_csv() to read in the file in 'ind_pop_data.csv' in chunks of size 1000. Assign the result to urb_pop_reader.
- Get the first DataFrame chunk from the iterable urb_pop_reader and assign this to df_urb_pop.
- Select only the rows of df_urb_pop that have a 'CountryCode' of 'CEB'. To do this, compare whether df_urb_pop['CountryCode'] 
is equal to 'CEB' within the square brackets in df_urb_pop[____].
- Using zip(), zip together the 'Total Population' and 'Urban population (% of total)' columns of df_pop_ceb. Assign the resulting zip object to pops.

Instructions - 3
- Use pd.read_csv() to read in the file 'ind_pop_data.csv' in chunks of size 1000. Assign the result to urb_pop_reader.
- Write a list comprehension to generate a list of values from pops_list for the new column 'Total Urban Population'. 
Use tup as the iterator variable. The output expression should be the product of the first and second element in each tuple in pops_list. 
Because the 2nd element is a percentage, you also need to either multiply the result by 0.01 or divide it by 100. In addition, note that the column 
'Total Urban Population' should only be able to take on integer values. To ensure this, make sure you cast the output expression to an integer with int().
- Create a scatter plot where the x-axis are values from the 'Year' column and the y-axis are values from the 'Total Urban Population' column.

Instructions - 4
- Initialize an empty DataFrame data using pd.DataFrame().
- In the for loop, iterate over urb_pop_reader to be able to process all the DataFrame chunks in the dataset.
- Using append() on data, append df_pop_ceb to data.

Instructions - 5
- Define the function plot_pop() that has two arguments: first is filename for the file to process and second is 
country_code for the country to be processed in the dataset.
- Call plot_pop() to process the data for country code 'CEB' in the file 'ind_pop_data.csv'.
- Call plot_pop() to process the data for country code 'ARB' in the file 'ind_pop_data.csv'.
'''

# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], 
            df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], 
            df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]
    
    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn, 'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(fn, 'ARB')