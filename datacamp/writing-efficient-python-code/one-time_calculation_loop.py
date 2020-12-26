'''
Instructions
- Import Counter from the collections module.
- Use Counter() to collect the count of each generation from the generations list. Save this as gen_counts.
- Write a better for loop that places a one-time calculation outside (above) the loop. Use the exact same 
syntax as the original for loop (simply copy and paste the one-time calculation above the loop).
'''

# Import Counter
from collections import Counter

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))

'''
Output:
generation 4: count = 112 percentage = 15.56
generation 1: count = 151 percentage = 20.97
generation 3: count = 136 percentage = 18.89
generation 5: count = 154 percentage = 21.39
generation 2: count =  99 percentage = 13.75
generation 6: count =  68 percentage = 9.44
'''