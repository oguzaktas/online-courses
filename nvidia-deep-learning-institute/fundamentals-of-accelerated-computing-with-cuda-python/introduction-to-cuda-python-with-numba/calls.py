# Use the 'File' menu above to 'Save' after pasting in your 3 function calls.
%%timeit
# Feel free to modify the 3 function calls in this cell
normalize(din_greyscales, out=d_normalized)
weigh(d_normalized, din_weights, out=d_weighted)
activate(d_weighted, out=dout_activated)
SOLUTION = dout_activated.copy_to_host()