'''
Instructions
- Create the DataFrame num_unique_labels by using the .apply() method on df[LABELS] with pd.Series.nunique as the argument.
- Create a bar plot of num_unique_labels using pandas' .plot(kind='bar') method.
- The axes have been labeled for you, so hit 'Submit Answer' to see the number of unique values for each label.
'''

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Calculate number of unique values for each label: num_unique_labels
num_unique_labels = df[LABELS].apply(pd.Series.nunique)

# Plot number of unique values for each label
num_unique_labels.plot(kind='bar')

# Label the axes
plt.xlabel('Labels')
plt.ylabel('Number of unique values')

# Display the plot
plt.show()
