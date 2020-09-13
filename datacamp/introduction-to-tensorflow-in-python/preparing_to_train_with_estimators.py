'''
High-level TensorFlow APIs -> Estimators
Mid-level TensorFlow APIs -> Layers, Datasets, Metrics
Low-level TensorFlow APIs -> Python
Estimators API -> high level submodule, less flexible, enforces best practices, faster deployment, many premade models

Model specification and training process with the Estimators API;
1. Define feature columns
2. Load and transform data
3. Define an estimator
4. Apply train operation

# Defining a numeric feature column
size = tf.feature_column.numeric_column("size")

# Loading and transforming data: Define input data function
def input_fn():
    # Define feature dictionary
    features = {"size": [1340, 1690, 2720], "rooms": [1, 3, 4]}
    # Define labels
    labels = [221900, 538000, 180000]
    return features, labels

# Define a deep neural network regression
model0 = tf.estimator.DNNRegressor(feature_columns=feature_list,\
hidden_units=[10, 6, 6, 3])
# Train the regression model
model0.train(input_fn, steps=20)
# Define a deep neural network classifier
model1 = tf.estimator.DNNClassifier(feature_columns=feature_list,\
hidden_units=[32, 16, 8], n_classes=4)
# Train the classifier
model1.train(input_fn, steps=20)
'''

'''
Instructions
- Complete the feature column for bedrooms and add another numeric feature column for bathrooms. Use bedrooms and bathrooms as the keys.
- Create a list of the feature columns, feature_list, in the order in which they were defined.
- Set labels to be equal to the price column in housing.
- Complete the bedrooms entry of the features dictionary and add another entry for bathrooms.
'''

# Define feature columns for bedrooms and bathrooms
bedrooms = feature_column.numeric_column("bedrooms")
bathrooms = feature_column.numeric_column("bathrooms")

# Define the list of feature columns
feature_list = [bedrooms, bathrooms]

def input_fn():
	# Define the labels
	labels = np.array(housing['price'])
	# Define the features
	features = {'bedrooms':np.array(housing['bedrooms']), 
                'bathrooms':housing['bathrooms']}
	return features, labels
