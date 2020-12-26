'''
Instructions
- Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them 
directly into the calc_win_perc() function. Store the result as a variable called win_percs_np.
- Create a new column in baseball_df called 'WP' that contains the win percentages you just calculated.
'''

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())