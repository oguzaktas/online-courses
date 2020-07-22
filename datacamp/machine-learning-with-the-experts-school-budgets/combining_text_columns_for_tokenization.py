'''
Instructions
- Use the .drop() method on data_frame with to_drop and axis= as arguments to drop the non-text data. Save the result as text_data.
- Fill in missing values (inplace) in text_data with blanks (""), using the .fillna() method.
- Complete the .apply() method by writing a lambda function that uses the .join() method to join all the items in a row with a space in between.
'''

# Define combine_text_columns()
def combine_text_columns(data_frame, to_drop=NUMERIC_COLUMNS + LABELS):
    """ converts all text in each row of data_frame to single vector """
    
    # Drop non-text columns that are in the df
    to_drop = set(to_drop) & set(data_frame.columns.tolist())
    text_data = data_frame.drop(to_drop, axis=1)
    
    # Replace nans with blanks
    text_data.fillna("", inplace=True)
    
    # Join all text items in a row that have a space in between
    return text_data.apply(lambda x: " ".join(x), axis=1)
