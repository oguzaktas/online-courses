'''
Instructions - 1
- Complete the function header of the nested function with the function name inner() and a single parameter word.
- Complete the return value: each element of the tuple should be a call to inner(), passing in the parameters from three_shouts() as arguments to each call.

Instructions - 2
- Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
- Complete the function echo() so that it returns inner_echo.
- We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. 
Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
- Hit Submit to call twice() and thrice() and print the results.
'''

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2) ,inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
