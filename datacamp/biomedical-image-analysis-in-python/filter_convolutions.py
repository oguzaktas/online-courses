'''
Instructions
- Create a three by three array of filter weights. Set each element to 0.11 to perform mean filtering (also called "uniform filtering").
- Convolve im with weights using ndi.convolve().
- Plot the original and mean-filtered images.
'''

# Set filter weights
weights = [[0.11, 0.11, 0.11],
           [0.11, 0.11, 0.11], 
           [0.11, 0.11, 0.11]]

# Convolve the image with the filter
im_filt = ndi.convolve(im, weights)

# Plot the images
fig, axes = plt.subplots(1,2)
axes[0].imshow(im)
axes[1].imshow(im_filt)
format_and_render_plot()
