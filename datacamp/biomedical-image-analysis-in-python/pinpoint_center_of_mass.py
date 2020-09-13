'''
Instructions
- Using vol and labels, calculate the center of mass for the two labeled objects. Print the coordinates.
- Use plt.scatter() to add the center of mass markers to the plot. Note that scatterplots 
draw from the bottom-left corner. Image columns correspond to x values and rows to y values.
'''

import matplotlib.pyplot as plt

# Extract centers of mass for objects 1 and 2
coms = ndi.center_of_mass(vol, labels, index=[1,2])
print('Label 1 center:', coms[0])
print('Label 2 center:', coms[1])

# Add marks to plot
for c0, c1, c2 in coms:
    plt.scatter(c2, c1, s=100, marker='o')
plt.show()
