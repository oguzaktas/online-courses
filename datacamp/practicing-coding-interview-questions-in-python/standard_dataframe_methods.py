'''
Instructions
- Load the data from the diabetes.csv file.
- Calculate the mean glucose level in the entire dataset.
- Group the data according to the diabetes test results.
- Calculate the mean glucose levels per group.
'''

# Load the data from the diabetes.csv file
diabetes = pd.read_csv('diabetes.csv')
print(diabetes.info())

# Calculate the mean glucose level in the entire dataset
print(diabetes['plasma glucose'].mean())

# Group the data according to the diabetes test results
diabetes_grouped = diabetes.groupby('test result')

# Calculate the mean glucose levels per group
print(diabetes_grouped['plasma glucose'].mean())

'''
Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
n pregnant           768 non-null int64
plasma glucose       763 non-null float64
blood pressure       733 non-null float64
skin thickness       541 non-null float64
serum insulin        394 non-null float64
bmi                  757 non-null float64
pedigree function    768 non-null float64
age                  768 non-null int64
test result          768 non-null object
dtypes: float64(6), int64(2), object(1)
memory usage: 54.1+ KB
None
121.6867627785059
test result
negative    110.643863
positive    142.319549
Name: plasma glucose, dtype: float64
'''