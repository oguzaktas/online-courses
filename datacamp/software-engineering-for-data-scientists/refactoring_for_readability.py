'''
Instructions
- Move the logic for calculating the perimeter into the polygon_perimeter function.
- Complete the definition of the polygon_apothem function, by moving the logic seen in the context. The math module has already been imported for you.
- Utilize the new unit functions to complete the definition of polygon_area.
- Use the more unitized polygon_area to calculate the area of a regular hexagon with legs of size 10.
'''

import math

def polygon_perimeter(n_sides, side_len):
    return n_sides * side_len

def polygon_apothem(n_sides, side_len):
    denominator = 2 * math.tan(math.pi / n_sides)
    return side_len / denominator

def polygon_area(n_sides, side_len):
    perimeter = polygon_perimeter(n_sides, side_len)
    apothem = polygon_apothem(n_sides, side_len)

    return perimeter * apothem / 2

# Print the area of a hexagon with legs of size 10
print(polygon_area(n_sides=6, side_len=10))
