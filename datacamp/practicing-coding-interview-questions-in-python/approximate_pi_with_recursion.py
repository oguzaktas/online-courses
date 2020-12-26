'''
Instructions
- Write a lambda expression calculating the k-th element in the series (without taking 4 into account).
- Specify the base case.
- Define the recursive call (n is the number of elements to consider).
'''

# Write an expression to get the k-th element of the series
get_elmnt = lambda k: (1 if k % 2 == 0 else -1) / (2 * k + 1) # get_elmnt = lambda k: ((-1)**k)/(2*k+1)

def calc_pi(n):
    curr_elmnt = get_elmnt(n)
    
    # Define the base case
    if n == 0:
    	return 4
      
    # Make the recursive call
    return 4 * curr_elmnt + calc_pi(n - 1)
  
# Compare the approximated Pi value to the theoretical one
print("approx = {}, theor = {}".format(calc_pi(500), math.pi))