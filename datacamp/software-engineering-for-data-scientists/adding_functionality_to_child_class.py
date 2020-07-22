'''
Instructions
- Fill in the first line ofSocialMedia's __init__ method using the parent class to properly utilize inheritance.
- Properly call the _count_mentions method in __init__ to add a new feature to SocialMedia.
'''

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')
