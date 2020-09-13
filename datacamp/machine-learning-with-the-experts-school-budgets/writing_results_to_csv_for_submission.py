'''
Instructions
- Create the prediction_df DataFrame by specifying the following arguments to the provided parameters pd.DataFrame():
    - pd.get_dummies(df[LABELS]).columns.
    - holdout.index.
    - predictions.
- Save prediction_df to a csv file called 'predictions.csv' using the .to_csv() method.
- Submit the predictions for scoring by using the score_submission() function with pred_path set to 'predictions.csv'.
'''

# Generate predictions: predictions
predictions = clf.predict_proba(holdout[NUMERIC_COLUMNS].fillna(-1000))

# Format predictions in DataFrame: prediction_df
prediction_df = pd.DataFrame(columns=pd.get_dummies(df[LABELS]).columns,
                             index=holdout.index,
                             data=predictions)


# Save prediction_df to csv
prediction_df.to_csv('predictions.csv')

# Submit the predictions for scoring: score
score = score_submission(pred_path='predictions.csv')

# Print score
print('Your model, trained with numeric data only, yields logloss score: {}'.format(score))
