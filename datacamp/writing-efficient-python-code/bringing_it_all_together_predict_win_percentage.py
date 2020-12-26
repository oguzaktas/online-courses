'''
Instructions
- Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function. 
Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.
- Apply predict_win_perc() to each row of the baseball_df DataFrame using a lambda function. Save the predicted win percentage as win_perc_preds_apply.
- Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df into predict_win_perc(). Save these predictions as win_perc_preds_np.
'''

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

'''
Output:
  Team League  Year   RS   RA   W    G  Playoffs    WP  WP_preds
0  ARI     NL  2012  734  688  81  162         0  0.50      0.53
1  ATL     NL  2012  700  600  94  162         1  0.58      0.58
2  BAL     AL  2012  712  705  93  162         1  0.57      0.50
3  BOS     AL  2012  734  806  69  162         0  0.43      0.45
4  CHC     NL  2012  613  759  61  162         0  0.38      0.39
'''