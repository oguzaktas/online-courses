# Add your completed `cuda_histogram` kernel definition here and save before running the assessment.
@cuda.jit
def cuda_histogram(x, xmin, xmax, histogram_out):
    '''Increment bin counts in histogram_out, given histogram range [xmin, xmax).'''
    bin_width = (xmax - xmin) / histogram_out.shape[0]
    
    start = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    for idx in range(start, x.shape[0], stride):
        bin_number = np.int32((x[idx]-xmin)/bin_width)
        if bin_number >= 0 and bin_number < histogram_out.shape[0]:
            cuda.atomic.add(histogram_out, bin_number, 1)