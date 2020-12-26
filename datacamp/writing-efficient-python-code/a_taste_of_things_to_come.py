'''
Instructions
- Print the list, new_list, that was created using a Non-Pythonic approach.
- A more Pythonic approach would loop over the contents of names, rather than using an index variable. Print better_list.
- The best Pythonic way of doing this is by using list comprehension. Print best_list.
'''

# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)