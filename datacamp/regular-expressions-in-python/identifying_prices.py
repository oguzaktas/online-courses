'''
Instructions
- Assign the first, second, and third element of tools to the variables our_tool, our_fee and our_pay respectively.
- Complete the template string using $tool, $fee, and $pay as identifiers. Add the dollar sign 
before the $fee identifier and add the characters ly directly after the $pay identifier.
- Substitute identifiers with the three variables you created and print out the results.
'''

# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))

'''
<script.py> output:
    We are offering a 3-month beginner course on Natural Language Toolkit just for $ 20 monthly
'''