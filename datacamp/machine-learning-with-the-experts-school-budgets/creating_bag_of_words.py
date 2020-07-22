'''
Instructions
- Import CountVectorizer from sklearn.feature_extraction.text.
- Fill missing values in df.Position_Extra using .fillna('') to replace NaNs with empty strings. Specify the additional 
keyword argument inplace=True so that you don't have to assign the result back to df.
- Instantiate the CountVectorizer as vec_alphanumeric by specifying the token_pattern to be TOKENS_ALPHANUMERIC.
- Fit vec_alphanumeric to df.Position_Extra.
- Hit 'Submit Answer' to see the len of the fitted representation as well as the first 15 elements, and compare to vec_basic.
'''

# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create the token pattern: TOKENS_ALPHANUMERIC
TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

# Fill missing values in df.Position_Extra
df.Position_Extra.fillna('', inplace=True)

# Instantiate the CountVectorizer: vec_alphanumeric
vec_alphanumeric = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC)

# Fit to the data
vec_alphanumeric.fit(df.Position_Extra)

# Print the number of tokens and first 15 tokens
msg = "There are {} tokens in Position_Extra if we split on non-alpha numeric"
print(msg.format(len(vec_alphanumeric.get_feature_names())))
print(vec_alphanumeric.get_feature_names()[:15])
