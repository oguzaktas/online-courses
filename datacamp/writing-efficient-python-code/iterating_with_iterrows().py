'''
Instructions
- Use .iterrows() to loop over pit_df and print each row. Save the first item from .iterrows() as i and the second as row.
- Add two lines to the loop: one before print(row) to print each index variable and one after to print each row's type.
- Instead of using i and row in the for statement to store the output of .iterrows(), use one variable named row_tuple.
- Add a line in the for loop to print the type of each row_tuple.
'''

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))

# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))