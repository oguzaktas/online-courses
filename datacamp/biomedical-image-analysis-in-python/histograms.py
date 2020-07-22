'''
Instructions
- Import scipy.ndimage as ndi.
- Generate a 256-bin histogram of im which covers the full range of np.uint8 values.
- Calculate the cumulative distribution function for im. First, 
find the cumulative sum of hist, then divide by the total number of pixels in hist.
- Plot hist and cdf on separate subplots. This has been done for you.
'''

import matplotlib.pyplot as plt

# Import SciPy's "ndimage" module
import scipy.ndimage as ndi 

# Create a histogram, binned at each possible value
hist = ndi.histogram(im, min=0, max=255, bins=256)

# Create a cumulative distribution function
cdf = hist.cumsum() / hist.sum()

# Plot the histogram and CDF
fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(hist, label='Histogram')
axes[1].plot(cdf, label='CDF')
format_and_render_plot()
