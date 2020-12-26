'''
Instructions
- Use .itertuples() to loop over rangers_df and print each row.
- Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.
- Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs.
'''

# Loop over the DataFrame and print each row
for row_tuple in rangers_df.itertuples():
  print(row_tuple)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

'''
Output:
Pandas(Index=0, Team='TEX', League='AL', Year=2012, RS=808, RA=707, W=93, G=162, Playoffs=1)
Pandas(Index=1, Team='TEX', League='AL', Year=2011, RS=855, RA=677, W=96, G=162, Playoffs=1)
Pandas(Index=2, Team='TEX', League='AL', Year=2010, RS=787, RA=687, W=90, G=162, Playoffs=1)
Pandas(Index=3, Team='TEX', League='AL', Year=2009, RS=784, RA=740, W=87, G=162, Playoffs=0)
Pandas(Index=4, Team='TEX', League='AL', Year=2008, RS=901, RA=967, W=79, G=162, Playoffs=0)
Pandas(Index=5, Team='TEX', League='AL', Year=2007, RS=816, RA=844, W=75, G=162, Playoffs=0)
Pandas(Index=6, Team='TEX', League='AL', Year=2006, RS=835, RA=784, W=80, G=162, Playoffs=0)
Pandas(Index=7, Team='TEX', League='AL', Year=2005, RS=865, RA=858, W=79, G=162, Playoffs=0)
Pandas(Index=8, Team='TEX', League='AL', Year=2004, RS=860, RA=794, W=89, G=162, Playoffs=0)
Pandas(Index=9, Team='TEX', League='AL', Year=2003, RS=826, RA=969, W=71, G=162, Playoffs=0)
Pandas(Index=10, Team='TEX', League='AL', Year=2002, RS=843, RA=882, W=72, G=162, Playoffs=0)
Pandas(Index=11, Team='TEX', League='AL', Year=2001, RS=890, RA=968, W=73, G=162, Playoffs=0)
Pandas(Index=12, Team='TEX', League='AL', Year=2000, RS=848, RA=974, W=71, G=162, Playoffs=0)
Pandas(Index=13, Team='TEX', League='AL', Year=1999, RS=945, RA=859, W=95, G=162, Playoffs=1)
Pandas(Index=14, Team='TEX', League='AL', Year=1998, RS=940, RA=871, W=88, G=162, Playoffs=1)
Pandas(Index=15, Team='TEX', League='AL', Year=1997, RS=807, RA=823, W=77, G=162, Playoffs=0)
Pandas(Index=16, Team='TEX', League='AL', Year=1996, RS=928, RA=799, W=90, G=163, Playoffs=1)
Pandas(Index=17, Team='TEX', League='AL', Year=1993, RS=835, RA=751, W=86, G=162, Playoffs=0)
Pandas(Index=18, Team='TEX', League='AL', Year=1992, RS=682, RA=753, W=77, G=162, Playoffs=0)
Pandas(Index=19, Team='TEX', League='AL', Year=1991, RS=829, RA=814, W=85, G=162, Playoffs=0)
Pandas(Index=20, Team='TEX', League='AL', Year=1990, RS=676, RA=696, W=83, G=162, Playoffs=0)
Pandas(Index=21, Team='TEX', League='AL', Year=1989, RS=695, RA=714, W=83, G=162, Playoffs=0)
Pandas(Index=22, Team='TEX', League='AL', Year=1988, RS=637, RA=735, W=70, G=161, Playoffs=0)
Pandas(Index=23, Team='TEX', League='AL', Year=1987, RS=823, RA=849, W=75, G=162, Playoffs=0)
Pandas(Index=24, Team='TEX', League='AL', Year=1986, RS=771, RA=743, W=87, G=162, Playoffs=0)
Pandas(Index=25, Team='TEX', League='AL', Year=1985, RS=617, RA=785, W=62, G=161, Playoffs=0)
Pandas(Index=26, Team='TEX', League='AL', Year=1984, RS=656, RA=714, W=69, G=161, Playoffs=0)
Pandas(Index=27, Team='TEX', League='AL', Year=1983, RS=639, RA=609, W=77, G=163, Playoffs=0)
Pandas(Index=28, Team='TEX', League='AL', Year=1982, RS=590, RA=749, W=64, G=162, Playoffs=0)
Pandas(Index=29, Team='TEX', League='AL', Year=1980, RS=756, RA=752, W=76, G=163, Playoffs=0)
Pandas(Index=30, Team='TEX', League='AL', Year=1979, RS=750, RA=698, W=83, G=162, Playoffs=0)
Pandas(Index=31, Team='TEX', League='AL', Year=1978, RS=692, RA=632, W=87, G=162, Playoffs=0)
Pandas(Index=32, Team='TEX', League='AL', Year=1977, RS=767, RA=657, W=94, G=162, Playoffs=0)
Pandas(Index=33, Team='TEX', League='AL', Year=1976, RS=616, RA=652, W=76, G=162, Playoffs=0)
Pandas(Index=34, Team='TEX', League='AL', Year=1975, RS=714, RA=733, W=79, G=162, Playoffs=0)
Pandas(Index=35, Team='TEX', League='AL', Year=1974, RS=690, RA=698, W=83, G=161, Playoffs=0)
Pandas(Index=36, Team='TEX', League='AL', Year=1973, RS=619, RA=844, W=57, G=162, Playoffs=0)
'''