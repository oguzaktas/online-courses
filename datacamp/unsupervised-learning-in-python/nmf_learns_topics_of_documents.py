'''
Instructions
- Import pandas as pd.
- Create a DataFrame components_df from model.components_, setting columns=words so that columns are labeled by the words.
- Print components_df.shape to check the dimensions of the DataFrame.
- Use the .iloc[] accessor on the DataFrame components_df to select row 3. Assign the result to component.
- Call the .nlargest() method of component, and print the result. This gives the five words with the highest values for that component.
'''

# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())
