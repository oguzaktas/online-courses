# Use the 'File' menu above to 'Save' after pasting in your own mm_shared function definition.
import numpy as np
from numba import cuda, types
@cuda.jit
def mm_shared(a, b, c):
    (row, column) = cuda.grid(2)
    tid_x, tid_y = cuda.threadIdx.x, cuda.threadIdx.y
    sum = 0

    # `a_cache` and `b_cache` are already correctly defined
    a_cache = cuda.shared.array(block_size, types.int32)
    b_cache = cuda.shared.array(block_size, types.int32)

    # TODO: use each thread to populate one element each in a_cache and b_cache
    a_cache[tid_x, tid_y] = a[row, tid_y]
    b_cache[tid_x, tid_y] = b[tid_x, column]
    
    cuda.syncthreads()
    
    for i in range(a.shape[1]):
        # TODO: calculate the `sum` value correctly using values from the cache 
        sum += a_cache[tid_x][i] * b_cache[i][tid_y]
        
    c[row][column] = sum