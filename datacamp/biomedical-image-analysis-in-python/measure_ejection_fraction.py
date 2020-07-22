'''
Instructions
- Get the index of the minimum and maximum volume images using np.argmin() and np.argmax().
- Plot the extreme volumes together. Display the images along the fifth plane, e.g. (vol_ts[t, 4]).
- Calculate the ejection volume and fraction using the min() and max() methods of ts. Print these values.
'''

import numpy as np

# Get index of max and min volumes
tmax = np.argmax(ts)
tmin = np.argmin(ts)

# Plot the largest and smallest volumes
fig, axes = plt.subplots(2,1)
axes[0].imshow(vol_ts[tmax, 4], vmax=160)
axes[1].imshow(vol_ts[tmin, 4], vmax=160)
format_and_render_plots()

# Calculate ejection fraction
ej_vol = ts.max() - ts.min()
ej_frac = ej_vol / ts.max()
print('Est. ejection volume (mm^3):', ej_vol)
print('Est. ejection fraction:', ej_frac)
