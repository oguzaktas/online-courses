'''
Instructions
- Initialize a mask with the same shape as the image, using np.zeros().
- In the mask, set the region that will be inpainted to 1 .
- Apply inpainting to image_with_logo using the mask.
'''

# Initialize the mask
mask = np.zeros(image_with_logo.shape[:-1])

# Set the pixels where the logo is to 1
mask[210:272, 360:425] = 1

# Apply inpainting to remove the logo
image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo, mask, multichannel=True)

# Show the original and logo removed images
show_image(image_with_logo, 'Image with logo')
show_image(image_logo_removed, 'Image with logo removed')
