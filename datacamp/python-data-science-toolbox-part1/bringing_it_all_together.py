'''
Instructions - 1
- In the filter() call, pass a lambda function and the sequence of tweets as strings, tweets_df['text']. 
The lambda function should check if the first 2 characters in a tweet x are 'RT'. Assign the resulting filter object to result. 
To get the first 2 characters in a tweet x, use x[0:2]. To check equality, use a Boolean filter with ==.
- Convert result to a list and print out the list.

Instructions - 2
- Add a try block so that when the function is called with the correct arguments, it processes the DataFrame and returns a dictionary of results.
- Add an except block so that when the function is called incorrectly, it displays the following error 
message: 'The DataFrame does not have a ' + col_name + ' column.'.

Instructions - 3
- If col_name is NOT a column in the DataFrame df, raise a ValueError 'The DataFrame does not have a ' + col_name + ' column.'.
- Call your new function count_entries() to analyze the 'lang' column of tweets_df. Store the result in result1.
- Print result1. This has been done for you, so hit 'Submit Answer' to check out the result.
- In the next exercise, you'll see that it raises the necessary ValueErrors.
'''

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang1')

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)
