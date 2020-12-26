'''
Instructions
- Create a boxplot of BMI indices for good and bad sides.
- Select rows from heroes for which the BMI index is smaller than 1000.
- Create a new boxplot of BMI indices for good and bad sides using heroes_filtered.
'''

import seaborn as sns

# Create a boxplot of BMI indices for 'good' and 'bad' sides
sns.boxplot(x='Alignment', y='bmi', data=heroes)
plt.show()

# Select rows from 'heroes' for which the BMI index < 1000
heroes_filtered = heroes[heroes['bmi'] < 1000]

# Create a new boxplot of BMI indices
sns.boxplot(x='Alignment', y='bmi', data=heroes_filtered)
plt.show()