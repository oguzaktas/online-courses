'''
Instructions
- Define the while loop as described in the context.
- Complete the return statement.
- Create a list of tuples defining pairs of coprime numbers from list1 and list2.
'''

def gcd(a, b):
    # Define the while loop as described
    while b != 0:
        temp_a = a
        a = b
        b = temp_a % b   
    # Complete the return statement
    return a
    
# Create a list of tuples defining pairs of coprime numbers
coprimes = [(i, j) for i in list1 
                 for j in list2 if gcd(i, j) == 1]
print(coprimes)