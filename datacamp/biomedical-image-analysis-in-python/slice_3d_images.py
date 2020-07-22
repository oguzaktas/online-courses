'''
Instructions
- Using plt.subplots(), initialize a subplots grid with 1 row and 4 columns.
- Plot every 40th slice of vol in grayscale. To get the appropriate index, multiply ii by 40.
- Turn off the ticks, labels, and frame for each subplot.
- Render the figure.
'''

import matplotlib.pyplot as plt

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=1, ncols=4)

# Loop through subplots and draw image
for ii in range(4):
    im = vol[ii*40, :, :]
    axes[ii].imshow(im, cmap='gray')
    axes[ii].axis('off')
    
# Render the figure
plt.show()
