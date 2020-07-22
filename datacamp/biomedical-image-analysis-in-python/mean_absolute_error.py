'''
Instructions
- Calculate the difference between im1 and im2.
- Plot err with the seismic colormap. To center the colormap at 0, set vmin=-200 and vmax=200.
- Compute the absolute error of the difference. Use np.abs(). Plot the image.
'''

# Calculate image difference
err = im1 - im2

# Plot the difference
plt.imshow(err, cmap='seismic', vmin=-200, vmax=200)
format_and_render_plot()

# Calculate absolute image difference
abs_err = np.abs(im1 - im2)

# Plot the difference
plt.imshow(abs_err, cmap='seismic', vmin=-200, vmax=200)
format_and_render_plot()

# Calculate mean absolute error
mean_abs_err = np.mean(np.abs(im1 - im2))
print('MAE:', mean_abs_err)
