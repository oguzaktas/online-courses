'''
Instructions
- Define the expression to rescale input series.
- Rescale the data in cols to lie between 1 and 10.
- Redefine the function to accept keyword arguments with 0 and 100 as the default lower and upper limit, respectively.
- Rescale the data in cols to lie between 1 and 10.
'''

def rescale(series, low, high):
   # Define the expression to rescale input series
   return series * (high - low) / 100 + low

# Rescale the data in cols to lie between 1 and 10
cols = ['math score', 'reading score', 'writing score'] 
scores[cols] = scores[cols].apply(rescale, args=[1, 10])
print(scores[cols].head())

# Redefine the function to accept keyword arguments
def rescale(series, low=0, high=100):
   return series * (high - low)/100 + low

'''
Output:
   math score  reading score  writing score
0        7.66           8.74           8.38
1        4.96           5.41           5.77
2        5.86           5.14           4.87
3        8.92           9.55           9.28
4        8.65           8.29           8.29
'''