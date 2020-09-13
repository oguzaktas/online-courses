'''
Instructions
- Apply ndi.sobel() to im along the first and second axes.
- Calculate the overall edge magnitude using the Pythagorean theorem. Use np.sqrt() and np.square().
- Display the magnitude image. Use a grayscale colormap and set vmax to 75.
'''

import matplotlib.pyplot as plt

# Apply Sobel filter along both axes
sobel_ax0 = ndi.sobel(im, axis=0)
sobel_ax1 = ndi.sobel(im, axis=1)

# Calculate edge magnitude 
edges = np.sqrt(np.square(sobel_ax0) + np.square(sobel_ax1))

# Plot edge magnitude
plt.imshow(edges, cmap='gray', vmax=75)
format_and_render_plot()
