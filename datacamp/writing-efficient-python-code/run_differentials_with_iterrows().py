'''
Instructions
- Create an empty list called run_diffs that will be used to store the run differentials you will calculate.
- Write a for loop that uses .iterrows() to loop over giants_df and collects each row's runs scored and runs allowed.
- Add a line to the for loop that uses the provided function to calculate each row's run differential.
- Add a line to the loop that appends each row's run differential to the run_diffs list.
'''

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)