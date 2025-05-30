'''
Instructions
- Inside the f-string, access the values of the keys price and date in east dictionary. Format the date to month-day-year.
- Inside the f-string, access the values of the keys price and date in west dictionary. Format the date to month-day-year.
'''

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")