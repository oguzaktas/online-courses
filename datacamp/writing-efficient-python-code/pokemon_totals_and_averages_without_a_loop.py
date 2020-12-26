'''
Instructions
- Replace the above for loop using NumPy:
    - Create a total stats array (total_stats_np) using the .sum() method and specifying the correct axis.
    - Create an average stats array (avg_stats_np) using the .mean() method and specifying the correct axis.
    - Create a final output list (poke_list_np) by combining the names list, the total_stats_np array, and the avg_stats_np array.
'''

# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

'''
Output:
[('Abomasnow', 494, 82.33333333333333), ('Abra', 310, 51.666666666666664), ('Absol', 465, 77.5)]
[('Abomasnow', 494, 82.33333333333333), ('Abra', 310, 51.666666666666664), ('Absol', 465, 77.5)] 

3 strongest Pokémon:
[('GroudonPrimal Groudon', 770, 128.33333333333334), ('KyogrePrimal Kyogre', 770, 128.33333333333334), ('Arceus', 720, 120.0)]
'''