'''
Instructions
- import your text_analyzer package.
- Create an instance of Document with the datacamp_tweet variable that's been loaded into your session.
- Print the contents of the text attribute of your newly created Document instance.
'''

# Import custom text_analyzer package
import text_analyzer

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)
