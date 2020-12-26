'''
Instructions
- Use the provided function to collect the unique Pokémon in the names list. Save this as uniq_names_func.
- Use a set data type to collect the unique Pokémon in the names list. Save this as uniq_names_set.
- Use the most efficient approach for gathering unique items to collect the unique Pokémon types 
(from the primary_types list) and Pokémon generations (from the generations list).
'''

# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types) 
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n') 