'''
Instructions
- Import ttest_ind from scipy.stats.
- Divide each patient's brain_vol by their skull_vol to create a normalized measure.
- Extract the adjusted brain measures from each group using df.loc.
- Calculate the t-statistic and p-value using ttest_ind. Be sure to pass in brain_alz first, followed by brain_typ.

'''

# Import independent two-sample t-test
from scipy.stats import ttest_ind

# Divide `df.brain_vol` by `df.skull_vol`
df['adj_brain_vol'] = df.brain_vol / df.skull_vol

# Select brain measures by Alzheimers group
brain_alz = df.loc[df.alzheimers == True, 'adj_brain_vol']
brain_typ = df.loc[df.alzheimers == False, 'adj_brain_vol']

# Evaluate null hypothesis
results = ttest_ind(brain_alz, brain_typ)
