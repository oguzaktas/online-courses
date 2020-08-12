'''
Instructions
- Create a 3x3 array of filter weights that detects when intensity changes from the left to right. Use only the values 1, 0 and -1.
- Convolve im with the edge detector.
- Plot the horizontal edges with the seismic colormap. Use vmin=-150 and vmax=150 to control adjust your colormap scale.
- Add a colorbar and render the results.
'''

# Set weights to detect vertical edges
weights = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]

# Convolve "im" with filter weights
edges = ndi.convolve(im, weights)

# Draw the image in color
plt.imshow(edges, cmap='seismic', vmin=-150, vmax=150)
plt.colorbar()
format_and_render_plot()
