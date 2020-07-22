# Use the 'File' menu above to 'Save' after pasting in your 3 function calls.
# Remember that we can't use numpy math function on the GPU...
from numpy import exp

# Consider modifying the 3 values in this cell to optimize host <-> device memory movement
normalized = np.empty_like(greyscales)
weighted = np.empty_like(greyscales)
activated = np.empty_like(greyscales)

# Modify these 3 function calls to run on the GPU
def normalize(grayscales):
    return grayscales / 255

def weigh(values, weights):
    return values * weights
        
def activate(values):
    return ( np.exp(values) - np.exp(-values) ) / ( np.exp(values) + np.exp(-values) )