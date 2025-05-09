'''
Instructions
- The math module has been pre-loaded into your environment to be able to use its sqrt function.
- Give function the best possible name from the following options: do_stuff, hypotenuse_length, square_root_of_leg_a_squared_plus_leg_b_squared, pythagorean_theorem.
- Complete the docstring's example with the function's name.
- print the result of using the newly named function to find the length of the hypotenuse for a right triangle with legs of length 6 & 8.
'''

import math

def hypotenuse_length(leg_a, leg_b):
    """Find the length of a right triangle's hypotenuse

    :param leg_a: length of one leg of triangle
    :param leg_b: length of other leg of triangle
    :return: length of hypotenuse
    
    >>> hypotenuse_length(3, 4)
    5
    """
    return math.sqrt(leg_a**2 + leg_b**2)


# Print the length of the hypotenuse with legs 6 & 8
print(hypotenuse_length(6, 8))
