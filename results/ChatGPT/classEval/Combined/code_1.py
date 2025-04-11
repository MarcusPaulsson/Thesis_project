import math

class AreaCalculator:
    """
    A class for calculating the area of different shapes, including circle, sphere, cylinder, sector, and annulus.
    """

    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        :param radius: float
        """
        self.radius = radius

    def calculate_circle_area(self):
        """
        Calculate the area of circle based on self.radius.
        :return: area of circle, float
        """
        return math.pi * (self.radius ** 2)

    def calculate_sphere_area(self):
        """
        Calculate the area of sphere based on self.radius.
        :return: area of sphere, float
        """
        return 4 * math.pi * (self.radius ** 2)

    def calculate_cylinder_area(self, height):
        """
        Calculate the surface area of cylinder based on self.radius and height.
        :param height: height of cylinder, float
        :return: surface area of cylinder, float
        """
        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        """
        Calculate the area of sector based on self.radius and angle.
        :param angle: angle of sector in radians, float
        :return: area of sector, float
        """
        return (angle / (2 * math.pi)) * self.calculate_circle_area()

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        Calculate the area of annulus based on inner_radius and outer_radius.
        :param inner_radius: inner radius of the annulus, float
        :param outer_radius: outer radius of the annulus, float
        :return: area of annulus, float
        """
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)
