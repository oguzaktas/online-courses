'''
Instructions
- Create a Boolean bone mask by selecting pixels greater than or equal to 145.
- Apply the mask to your image using np.where(). Values not in the mask should be set to 0.
- Create a histogram of the masked image. Use the following arguments to select only non-zero pixels: min=1, max=255, bins=255.
- Plot the masked image and the histogram. This has been done for you.
'''

import matplotlib.pyplot as plt

# Import SciPy's "ndimage" module
import scipy.ndimage as ndi

# Screen out non-bone pixels from "im"
mask_bone = im >= 145
im_bone = np.where(mask_bone, im, 0)

# Get the histogram of bone intensities
hist = ndi.histogram(im_bone, min=1, max=255, bins=255)

# Plot masked image and histogram
fig, axes = plt.subplots(2,1)
axes[0].imshow(im_bone)
axes[1].plot(hist)
format_and_render_plot()
