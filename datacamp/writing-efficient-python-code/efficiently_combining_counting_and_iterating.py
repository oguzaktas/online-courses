# Counting with loop
poke_types = ['Grass', 'Dark', 'Fire', 'Fire', 'Water', 'Fire']
type_counts = {}
for poke_type in poke_types:
    if poke_type not in type_counts:
        type_counts[poke_type] = 1
    else:
        type_counts[poke_type] += 1
print(type_counts)

# Counting with collections.Counter()
from collections import Counter
type_counts = Counter(poke_types) # Result is counter dictionary

# Combinations with loop
combos = []
for x in poke_types:
    for y in poke_types:
        if x == y:
            continue
        if ((x,y) not in combos) & ((y,x) not in combos):
            combos.append((x,y))
print(combos)

# itertools.combinations()
from itertools import combinations
combos_obj = combinations(poke_types, 2)
print(type(combos_obj))
combos = [*combos_obj]
print(combos)