'''
Instructions
- Import ttest_ind() from scipy.stats.
- Create a vector of 'brain_vol' values for each of the Alzheimer's Disease and Typical Elderly groups.
- Use ttest_ind() to test for differences between the two groups' 'gray_vol' metrics. Print the results.
- Visualize the 'brain_vol' measures using the boxplot() method of df. 
Group the variables by their disease classification by setting by='alzheimers'.
'''

# Import independent two-sample t-test
from scipy.stats import ttest_ind

# Select data from "alzheimers" and "typical" groups
brain_alz = df.loc[df.alzheimers == True, 'brain_vol']
brain_typ = df.loc[df.age > 70, 'brain_vol']
# or brain_typ = df.loc[df.alzheimers == False, 'brain_vol']

# Perform t-test of "alz" > "typ"
results = ttest_ind(brain_alz, brain_typ)
print('t = ', results.statistic)
print('p = ', results.pvalue)

# Show boxplot of brain_vol differences
df.boxplot(column='brain_vol', by='alzheimers')
plt.show()
