import numpy as np

names = ['Absol', 'Aron', 'Jynx', 'Natu', 'Onix']
attacks = np.array([130, 70, 50, 50, 45])

# Calculate total average once (outside the loop)
total_attack_avg = attacks.mean()

for pokemon, attack in zip(names, attacks):
    if attack > total_attack_avg:
        print(
            "{}'s attack: {} > average: {}!".format(pokemon, attack, total_attack_avg)
        )

# Using holistic conversions
names = ['Pikachu', 'Squirtle', 'Articuno']
legend_status = [False, False, True]
generations = [1, 1, 1]
poke_data = []
for poke_tuple in zip(names, legend_status, generations):
    poke_list = list(poke_tuple)
    poke_data.append(poke_list)
print(poke_data)
'''
poke_data_tuples = []
for poke_tuple in zip(names, legend_status, generations):
    poke_data_tuples.append(poke_tuple)
poke_data = [*map(list, poke_data_tuples)]
print(poke_data)
'''