'''
Instructions
- Create the labels array from mask, then create a mask left ventricle pixels. 
(Use the coordinates 128, 128 to find the left ventricle label value.)
- Find the bounding box indices for lv_mask. Print the number of objects found and the values for the first box.
- Select the portion of im that is within the left ventricle bounding box.
- Plot the cropped image.
'''

# Create left ventricle mask
labels, nlabels = ndi.label(mask)
lv_val = labels[128, 128]
lv_mask = np.where(labels == lv_val, 1, 0)

# Find bounding box of left ventricle
bboxes = ndi.find_objects(lv_mask)
print('Number of objects:', len(bboxes))
print('Indices for first box:', bboxes[0])

# Crop to the left ventricle (index 0)
im_lv = im[bboxes[0]]

# Plot the cropped image
plt.imshow(im_lv)
format_and_render_plot()
