'''
Instructions
- Exclude all the numbers from nums divisible by 3 or 5.
- Return the string without its vowels ('y' is not a vowel in this case).
- Filter all the spells in spells with more than two 'a' characters.
'''

# Exclude all the numbers from nums divisible by 3 or 5
print(nums)
fnums = filter(lambda x: x % 3 != 0 and x % 5 != 0, nums)
print(list(fnums))

# Return the string without its vowels
print(string)
vowels = ['a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I']
fstring = filter(lambda c: c not in vowels, string)
print(''.join(fstring))

# Filter all the spells in spells with more than two 'a's
print(spells)
fspells = filter(lambda s: s.count('a') > 2, spells)
print(list(fspells))