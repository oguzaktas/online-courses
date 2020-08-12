'''
Instructions - 1
- Import:
    - NMF from sklearn.decomposition.
    - Normalizer and MaxAbsScaler from sklearn.preprocessing.
    - make_pipeline from sklearn.pipeline.
- Create an instance of MaxAbsScaler called scaler.
- Create an NMF instance with 20 components called nmf.
- Create an instance of Normalizer called normalizer.
- Create a pipeline called pipeline that chains together scaler, nmf, and normalizer.
- Apply the .fit_transform() method of pipeline to artists. Assign the result to norm_features.

Instructions - 2
- Import pandas as pd.
- Create a DataFrame df from norm_features, using artist_names as an index.
- Use the .loc[] accessor of df to select the row of 'Bruce Springsteen'. Assign the result to artist.
- Apply the .dot() method of df to artist to calculate the dot product of every row with artist. Save the result as similarities.
- Print the result of the .nlargest() method of similarities to display the artists most similar to 'Bruce Springsteen'.
'''

# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)

# Import pandas
import pandas as pd

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=artist_names)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())
