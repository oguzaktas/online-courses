'''
Instructions
- Group the data by the two factors specified above.
- Filter groups having more than 10 valid bmi observations.
- Group the filtered data again by the same factors.
- Calculate the mean and standard deviation of the BMI index.
'''

import numpy as np

# Group the data by two factors specified in the context
groups = heroes.groupby(['Alignment', 'Publisher'])

# Filter groups having more than 10 valid bmi observations
fheroes = groups.filter(lambda x: x['bmi'].count() > 10)

# Group the filtered data again by the same factors
fgroups = fheroes.groupby(['Alignment', 'Publisher'])

# Calculate the mean and standard deviation of the BMI index
result = fgroups['bmi'].agg([np.mean, np.std])
print(result)

'''
Output:
<script.py> output:
                                  mean         std
    Alignment Publisher                           
    bad       DC Comics      71.460251  250.642060
              Marvel Comics  62.512261  258.935100
    good      DC Comics      25.028215    6.879312
              Marvel Comics  28.968076   16.550686
'''