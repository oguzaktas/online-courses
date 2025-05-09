'''
Instructions
- import the needed function, setup, from the setuptools package.
- List yourself as the author.
- Specify your install_requires to require matplotlib version 3.0.0 or above.
'''

# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='oguz',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])
