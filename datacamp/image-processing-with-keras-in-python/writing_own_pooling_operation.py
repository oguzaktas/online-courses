'''
Instructions
- Index into the input array (im) and select the right window.
- Find the maximum in this window.
- Allocate this into the right entry in the output array (result).
'''

# Result placeholder
result = np.zeros((im.shape[0]//2, im.shape[1]//2))

# Pooling operation
for ii in range(result.shape[0]):
    for jj in range(result.shape[1]):
        result[ii, jj] = np.max(im[ii*2:ii*2+2, jj*2:jj*2+2])
