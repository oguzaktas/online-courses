'''
Instructions
- Write a regular expression to match valid passwords as described.
- Scan the elements in the passwords list to find out if they are valid passwords.
- To print out the message indicating if it is a valid password or not, complete .format() statement.
'''

# Write a regex to match a valid password
regex = r"[a-zA-Z0-9*#$%!&.]{8,20}"

for example in passwords:
  	# Scan the strings to find a match
    if re.search(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))   

'''
<script.py> output:
    The password Apple34!rose is a valid password
    The password My87hou#4$ is a valid password
    The password abc123 is invalid
'''