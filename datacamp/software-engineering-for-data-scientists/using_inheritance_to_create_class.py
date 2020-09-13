'''
Instructions
- Document has been preloaded in the session.
- Complete the class statement to create a SocialMedia class that inherits from Document.
- Define SocialMedia's __init__() method that initializes a Document.
'''

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
