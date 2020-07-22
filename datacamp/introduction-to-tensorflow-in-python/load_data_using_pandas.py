'''
Instructions
- Import pandas under the alias pd.
- Assign the path to a string variable with the name data_path.
- Load the dataset as a pandas dataframe named housing.
- Print the price column of housing.
'''

'''
Setting the data type
# Load KC dataset
housing = pd.read_csv('kc_housing.csv')

# Convert price to column to float32
price = np.array(housing['price'], np.float32)
# price = tf.cast(housing['price'], tf.float32)

# Convert waterfront column to Boolean
waterfront = np.array(housing['waterfront'], np.bool)
# waterfront = tf.cast(housing['waterfront'], tf.bool)
'''

# Import pandas under the alias pd
import pandas as pd

# Assign the path to a string variable named data_path
data_path = 'kc_house_data.csv'

# Load the dataset as a dataframe named housing
housing = pd.read_csv(data_path)

# Print the price column of housing
print(housing['price'])
