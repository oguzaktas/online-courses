'''
Instructions
- Write a regular expression to match valid email addresses as described.
- Match the regex to the elements contained in emails.
- To print out the message indicating if it is a valid email or not, complete .format() statement.
'''

# Write a regex to match a valid email address
regex = r"[a-zA-Z0-9!#%&*$.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))   

'''
Output:
The email n.john.smith@gmail.com is a valid email
The email 87victory@hotmail.com is a valid email
The email !#mary-=@msca.net is invalid
'''