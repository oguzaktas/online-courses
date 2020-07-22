# Use the 'File' menu above to 'Save' after pasting in your imports, data, and function definitions.
n = 1000000

greyscales = np.floor(np.random.uniform(0, 255, n).astype(np.float32))
weights = np.random.normal(.5, .1, n).astype(np.float32)