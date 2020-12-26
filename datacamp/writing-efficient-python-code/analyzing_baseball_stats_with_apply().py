'''
Instructions
- Apply sum() to each column of rays_df to collect the sum of each column. Be sure to specify the correct axis.
- Apply sum() to each row of rays_df, only looking at the 'RS' and 'RA' columns, and specify the correct axis.
- Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.
'''

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=1)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

'''
Output:
RS          3783
RA          3265
W            458
Playoffs       3
dtype: int64

2012    1274
2011    1321
2010    1451
2009    1557
2008    1445
dtype: int64

2012     No
2011    Yes
2010    Yes
2009     No
2008    Yes
dtype: object
'''