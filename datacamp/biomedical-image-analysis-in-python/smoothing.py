'''
Instructions
- Convolve im with Gaussian filters of size sigma=1 and sigma=3.
- Plot the "bone masks" of im, im_s1, and im_s3 (i.e., where intensities are greater than or equal to 145).
'''

# Smooth "im" with Gaussian filters
im_s1 = ndi.gaussian_filter(im, sigma=1)
im_s3 = ndi.gaussian_filter(im, sigma=3)

# Draw bone masks of each image
fig, axes = plt.subplots(1,3)
axes[0].imshow(im >= 145)
axes[1].imshow(im_s1 >= 145)
axes[2].imshow(im_s3 >= 145)
plt.show()
format_and_render_plot()
