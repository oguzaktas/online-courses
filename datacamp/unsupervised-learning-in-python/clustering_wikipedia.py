'''
Instructions - 1
- Import:
    - TruncatedSVD from sklearn.decomposition.
    - KMeans from sklearn.cluster.
    - make_pipeline from sklearn.pipeline.
- Create a TruncatedSVD instance called svd with n_components=50.
- Create a KMeans instance called kmeans with n_clusters=6.
- Create a pipeline called pipeline consisting of svd and kmeans.

Instructions - 2
- Import pandas as pd.
- Fit the pipeline to the word-frequency array articles.
- Predict the cluster labels.
- Align the cluster labels with the list titles of article titles by creating a DataFrame df with labels and titles as columns. This has been done for you.
- Use the .sort_values() method of df to sort the DataFrame by the 'label' column, and print the result.
- Hit 'Submit Answer' and take a moment to investigate your amazing clustering of Wikipedia pages!
'''

# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)

# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))
