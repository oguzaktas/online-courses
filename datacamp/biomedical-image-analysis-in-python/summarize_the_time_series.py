'''
Instructions
- Initialize an empty array with 20 elements using np.zeros().
- Calculate the volume of each image voxel. (Consult the meta dictionary for sampling rates.)
- For each time point, count the pixels in labels, and update the time series array.
- Plot the time series using plt.plot().
'''

import numpy as np

# Create an empty time series
ts = np.zeros(20)

# Calculate volume at each voxel
d0, d1, d2, d3 = vol_ts.meta['sampling']
dvoxel = d1 * d2 * d3

# Loop over the labeled arrays
for t in range(20):
    nvoxels = ndi.sum(1, labels[t], index=1)
    ts[t] = nvoxels * dvoxel

# Plot the data
plt.plot(ts)
format_and_render_plot()
