'''
Instructions
- combinations from the itertools module has been loaded into your session. Use it to create a list called 
possible_pairs that contains all possible pairs of Pokémon types (each pair has 2 Pokémon types).
- Create an empty list called enumerated_tuples above the for loop.
- Within the for loop, append each enumerated_pair_tuple to the empty list you created in the above step.
- Use a built-in function to convert each tuple in enumerated_tuples to a list.
'''

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)