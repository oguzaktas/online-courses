'''
Instructions
- Use range() to create a list of arrival times (10 through 50 incremented by 10). Create the list arrival_times by unpacking the range object.
- You realize your clock is three minutes fast. Convert the arrival_times list into a numpy array 
(called arrival_times_np) and use NumPy broadcasting to subtract three minutes from each arrival time.
- Use list comprehension with enumerate() to pair each guest in the names list to their updated arrival time in the 
new_times array. You'll need to use the index variable created from using enumerate() on new_times to index the names list.
- A function named welcome_guest() has been pre-loaded into your session. Use map() to apply 
this function to each element of the guest_arrivals list and save it as the variable welcome_map.
'''

import numpy as np

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')