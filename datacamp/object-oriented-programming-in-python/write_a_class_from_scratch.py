import numpy as np


# Write the class Point as outlined in the instructions
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)

    def reflect(self, axis):
        if axis == "x":
            self.y = -self.y
        if axis == "y":
            self.x = -self.x
