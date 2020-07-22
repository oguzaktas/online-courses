'''
Instructions
- Use ndi.label() to assign labels to each separate object in mask.
- Find the index value for the left ventricle label by checking the center pixel (128, 128).
- Create a mask of pixels matching the left ventricle label. Using np.where, set pixels labeled as lv_val to 1 and other values to np.nan.
- Use plt.imshow() to overlay the selected label on the current plot.
'''

# Label the image "mask"
labels, nlabels = ndi.label(mask)

# Select left ventricle pixels
lv_val = labels[128, 128]
lv_mask = np.where(labels == lv_val, 1, np.nan)

# Overlay selected label
plt.imshow(lv_mask, cmap='rainbow')
plt.show()
