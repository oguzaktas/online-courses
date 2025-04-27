# Create a SelectorList of the course titles
crs_title_els = response.xpath('//h4/text()')

# Extract the course titles
crs_titles = crs_title_els.extract()

# Print out the course titles
for el in crs_titles:
  print( ">>", el )