'''
Instructions
- Import the inpaint function in the restoration module in scikit-image (skimage).
- Show the defective image using show_image().
- Call the correct function from inpaint. Use the corrupted image as the first parameter, then the mask and multichannel boolean.
'''

# Import the module from restoration
from skimage.restoration import inpaint

# Show the defective image
show_image(defect_image, 'Image to restore')

# Apply the restoration function to the image using the mask
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, multichannel=True)
show_image(restored_image)
