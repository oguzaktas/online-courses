# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)