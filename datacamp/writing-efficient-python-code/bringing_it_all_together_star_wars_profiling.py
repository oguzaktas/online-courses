'''
Instructions
- Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect 
heroes from the Star Wars universe. The desired_publisher for Star Wars is 'George Lucas'.
'''

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

'''
%load_ext line_profiler
%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
'''

'''
from hero_funcs import get_publisher_heroes, get_publisher_heroes_np

%load_ext memory_profiler

%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
'''