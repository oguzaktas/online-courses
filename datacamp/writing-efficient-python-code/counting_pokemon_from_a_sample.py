'''
Instructions
- Collect the count of each primary type from the sample.
- Collect the count of each generation from the sample.
- Use list comprehension to collect the first letter of each Pokémon in the names list. Save this as starting_letters.
- Collect the count of starting letters from the starting_letters list. Save this as starting_letters_count.
'''

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)