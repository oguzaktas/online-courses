# Use the 'File' menu above to 'Save' after pasting in your imports, data, and function definitions.
# Remember that we can't use numpy math function on the GPU...
import numpy as np
import math
from numba import cuda
from numba import vectorize

# Consider modifying the 3 values in this cell to optimize host <-> device memory movement
din_greyscales = cuda.to_device(greyscales)
din_weights = cuda.to_device(weights)

d_normalized = cuda.device_array(shape=(n,), dtype=np.float32)
d_weighted = cuda.device_array(shape=(n,), dtype=np.float32)
dout_activated = cuda.device_array(shape=(n,), dtype=np.float32)

# Modify these 3 function calls to run on the GPU
@vectorize(['float32(float32)'], target='cuda')
def normalize(grayscales):
    return grayscales / 255

@vectorize(['float32(float32, float32)'], target='cuda')
def weigh(values, weights):
    return values * weights

@vectorize(['float32(float32)'], target='cuda')
def activate(values):
    return (math.exp(values) - math.exp(-values)) / (math.exp(values) + math.exp(-values))