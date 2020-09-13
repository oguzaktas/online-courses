'''
Instructions
- First of all, import Template from string module.
- Complete the template using $tool and $description identifiers.
- Substitute identifiers with the correct tool and description variables in the template and print out the results.
'''

# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1))
print(wikipedia.substitute(tool=tool2, description=description2))
print(wikipedia.substitute(tool=tool3, description=description3))