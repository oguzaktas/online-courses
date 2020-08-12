'''
Instructions
- Obtain the red channel using slicing.
- Plot the histogram and bins in a range of 256.
'''

# Obtain the red channel
red_channel = image[:, :, 0]

# Plot the red histogram with bins in a range of 256
plt.hist(red_channel.ravel(), bins=256)

# Set title and show
plt.title('Red Histogram')
plt.show()
