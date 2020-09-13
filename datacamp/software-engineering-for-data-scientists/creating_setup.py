'''
Instructions
- import the needed function, setup, from the setuptools package.
- Complete the name & packages arguments; keep in mind your package is located in a directory named text_analyzer.
- List yourself as the author.
'''

# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='oguz',
      packages=['text_analyzer'])
