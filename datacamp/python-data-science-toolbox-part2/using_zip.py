'''
Instructions
- Using zip() with list(), create a list of tuples from the three lists mutants, aliases, and powers (in that order) and assign the result to mutant_data.
- Using zip(), create a zip object called mutant_zip from the three lists mutants, aliases, and powers.
- Complete the for loop by unpacking the zip object you created and printing the tuple values.
- Use value1, value2, value3 for the values from each of mutants, aliases, and powers, in that order.
'''

# Provided lists
mutants = ['charles xavier', 'bobby drake',
           'kurt wagner', 'max eisenhardt', 'kitty pride']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis',
          'teleportation', 'magnetokinesis', 'intangibility']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
