'''
Instructions
- Create a mask of left ventricle pixels (Value of 1 in labels).
- Calculate the distance to background for each pixel using ndi.distance_transform_edt(). Supply pixel dimensions to the sampling argument.
- Print out the maximum distance and its coordinates using ndi.maximum and ndi.maximum_position.
- Overlay a slice of the distance map on the original image. This has been done for you.
'''

import numpy as np

# Calculate left ventricle distances
lv = np.where(labels == 1, 1, 0)
dists = ndi.distance_transform_edt(lv)

# Report on distances
print('Max distance (mm):', ndi.maximum(dists))
print('Max location:', ndi.maximum_position(dists))

# Plot overlay of distances
overlay = np.where(dists[5] > 0, dists[5], np.nan) 
plt.imshow(overlay, cmap='hot')
format_and_render_plot()
