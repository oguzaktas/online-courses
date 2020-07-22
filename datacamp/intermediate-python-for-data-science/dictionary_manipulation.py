'''
Instructions - 1
- Add the key 'italy' with the value 'rome' to europe.
- To assert that 'italy' is now a key in europe, print out 'italy' in europe.
- Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
- Print out europe.

Instructions - 2
- The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
- Australia is not in Europe, Austria is! Remove they key 'australia' from europe.
- Print out europe to see if your cleaning work paid off.
'''

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe["italy"] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe["poland"] = 'warsaw'

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)
