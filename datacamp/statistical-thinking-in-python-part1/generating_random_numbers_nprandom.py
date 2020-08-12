'''
Instructions
- Seed the random number generator using the seed 42.
- Initialize an empty array, random_numbers, of 100,000 entries to store the random numbers. Make sure you use np.empty(100000) to do this.
- Write a for loop to draw 100,000 random numbers using np.random.random(), storing them in the random_numbers array. To do so, loop over range(100000).
- Plot a histogram of random_numbers. It is not necessary to label the axes in this case because 
we are just checking the random number generator. Hit 'Submit Answer' to show your plot.
'''

import numpy as np
import matplotlib.pyplot as plt

# Seed the random number generator
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()
    print(random_numbers[i])

# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()
