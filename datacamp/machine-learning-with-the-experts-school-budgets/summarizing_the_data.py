'''
Instructions
- Print summary statistics of the numeric columns in the DataFrame df using the .describe() method.
- Import matplotlib.pyplot as plt.
- Create a histogram of the non-null 'FTE' column. You can do this by passing df['FTE'].dropna() to plt.hist().
- The title has been specified and axes have been labeled, so hit 'Submit Answer' to see how often school employees work full-time!
'''

# Print the summary statistics
print(df.describe())

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Create the histogram
plt.hist(df['FTE'].dropna())

# Add title and labels
plt.title('Distribution of %full-time \n employee works')
plt.xlabel('% of full-time')
plt.ylabel('num employees')

# Display the histogram
plt.show()
