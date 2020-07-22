'''
Instructions
- Slice a 2D plane from vol where "axis 1" is 256.
- Slice a 2D plane from vol where "axis 2" is 256.
- For each image, calculate the aspect ratio by dividing the image "sampling" rate 
for axis 0 by its opponent axis. This information is in vol.meta.
'''

# Select frame from "vol"
im1 = vol[:, 256, :]
im2 = vol[:, :, 256]

# Compute aspect ratios
d0, d1, d2 = vol.meta['sampling']
asp1 = d0 / d2
asp2 = d0 / d1

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].imshow(im1, cmap='gray', aspect=asp1)
axes[1].imshow(im2, cmap='gray', aspect=asp2)
plt.show()
