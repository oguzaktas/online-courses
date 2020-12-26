'''
Instructions
- Define the initial check: numbers lower than 2 are not prime.
- Define the loop checking if the number n is not prime.
- Filter prime numbers from cands into the primes list.
'''

def is_prime(n):
    # Define the initial check
    if n < 2:
       return False
    # Define the loop checking if a number is not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
# Filter prime numbers into the new list
primes = [num for num in cands if is_prime(num)]
print("primes = " + str(primes))