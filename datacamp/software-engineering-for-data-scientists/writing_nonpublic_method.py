'''
Instructions
- Counter from collections has been loaded into your environment, as well as the function tokenize().
- Add a method named count_words as a non-public method.
- Give your non-public method the functionality to count the contents tokens attribute using Counter().
- Utilize your new function in the __init__ method.
'''

class Document:
  def __init__(self, text):
    self.text = text
    # Tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # Perform word count with non-public count_words method
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text)
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)
