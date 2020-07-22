'''
Instructions
- Import pandas as pd.
- Create a DataFrame df from nmf_features using pd.DataFrame(). Set the index to titles using index=titles.
- Use the .loc[] accessor of df to select the row with title 'Anne Hathaway', and print the result. 
These are the NMF features for the article about the actress Anne Hathaway.
- Repeat the last step for 'Denzel Washington' (another actor).
'''

# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])
