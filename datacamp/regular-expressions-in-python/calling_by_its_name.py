'''
Instructions
- Create a dictionary assigning the first and second element appearing in the list courses to the keys "field" and "tool" respectively.
- Complete the placeholders accessing inside to the elements linked with the keys field and tool in the dictionary data.
- Print out the resulting message using the .format() method, passing the plan dictionary to replace the data placeholders.
'''

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use dictionary to replace placeholders
print(my_message.format(data=plan))

'''
<script.py> output:
    If you are interested in artificial intelligence, you can take the course related to neural networks
'''