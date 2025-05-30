'''
Instructions
- Import HashingVectorizer from sklearn.feature_extraction.text.
- Instantiate the HashingVectorizer as hashing_vec using the TOKENS_ALPHANUMERIC pattern.
- Fit and transform hashing_vec using text_data. Save the result as hashed_text.
- Hit 'Submit Answer' to see some of the resulting hash values.
'''

# Import HashingVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

# Get text data: text_data
text_data = combine_text_columns(X_train)

# Create the token pattern: TOKENS_ALPHANUMERIC
TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)' 

# Instantiate the HashingVectorizer: hashing_vec
hashing_vec = HashingVectorizer(token_pattern=TOKENS_ALPHANUMERIC)

# Fit and transform the Hashing Vectorizer
hashed_text = hashing_vec.fit_transform(text_data)

# Create DataFrame and print the head
hashed_df = pd.DataFrame(hashed_text.data)
print(hashed_df.head())
