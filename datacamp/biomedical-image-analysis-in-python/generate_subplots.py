'''
Instructions
- Create a subplots grid where nrows=2 and ncols=1.
- Draw im1 and im2 on the first and second subplots respectively. Use a "gray" colormap for each.
- For each subplot, turn off the axis ticks and labels.
- Render the figure.
'''

# Import PyPlot
import matplotlib.pyplot as plt

# Initialize figure and axes grid
fig, axes = plt.subplots(nrows=2, ncols=1)

# Draw an image on each subplot
axes[0].imshow(im1, cmap='gray')
axes[1].imshow(im2, cmap='gray')

# Remove ticks/labels and render
axes[0].axis('off')
axes[1].axis('off')
plt.show()
