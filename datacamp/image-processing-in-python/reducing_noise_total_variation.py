'''
Instructions
- Import the denoise_tv_chambolle function from its module.
- Apply total variation filter denoising.
- Show the original noisy and the resulting denoised image.
'''

# Import the module and function
from skimage.restoration import denoise_tv_chambolle

# Apply total variation filter denoising
denoised_image = denoise_tv_chambolle(noisy_image, 
                                      multichannel=True)

# Show the noisy and denoised images
show_image(noisy_image, 'Noisy')
show_image(denoised_image, 'Denoised image')
