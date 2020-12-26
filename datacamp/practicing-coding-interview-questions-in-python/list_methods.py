'''
Instructions
- Remove fruits from basket2 that are already present in basket1.
- Transfer fruits from basket1 to basket2 until the amount in basket2 becomes more or equal to the amount in basket1.
'''

# Remove fruits from basket2 that are present in basket1
for item in basket1:
    if item in basket2:
        basket2.remove(item)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

# Transfer fruits from basket1 to basket2
while len(basket2) < len(basket1):
    item_to_transfer = basket1.pop()
    basket2.append(item_to_transfer)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))