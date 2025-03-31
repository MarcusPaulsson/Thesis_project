import math

class AreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_sphere_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def calculate_cylinder_area(self, height):
        return (2 * math.pi * self.radius * height) + (2 * math.pi * (self.radius ** 2))

    def calculate_sector_area(self, angle):
        return (angle / 360) * math.pi * (self.radius ** 2)

    def calculate_annulus_area(self, inner_radius, outer_radius):
        return math.pi * ((outer_radius ** 2) - (inner_radius ** 2))