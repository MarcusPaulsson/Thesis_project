import math

class AreaCalculator:
    """
    A class for calculating the area of various shapes, including circle, sphere, cylinder, sector, and annulus.
    """

    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        :param radius: float
        """
        self.radius = radius

    def calculate_circle_area(self):
        """
        Calculate the area of a circle based on self.radius.
        :return: area of circle, float
        """
        return math.pi * (self.radius ** 2)

    def calculate_sphere_area(self):
        """
        Calculate the surface area of a sphere based on self.radius.
        :return: area of sphere, float
        """
        return 4 * math.pi * (self.radius ** 2)

    def calculate_cylinder_area(self, height):
        """
        Calculate the surface area of a cylinder based on self.radius and height.
        :param height: height of cylinder, float
        :return: area of cylinder, float
        """
        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        """
        Calculate the area of a sector based on self.radius and angle.
        :param angle: angle of sector in radians, float
        :return: area of sector, float
        """
        return 0.5 * self.radius ** 2 * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        Calculate the area of an annulus based on inner_radius and outer_radius.
        :param inner_radius: inner radius of annulus, float
        :param outer_radius: outer radius of annulus, float
        :return: area of annulus, float
        """
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)

