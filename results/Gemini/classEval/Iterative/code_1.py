import math

class AreaCalculator:
    """
    This is a class for calculating the area of different shapes.
    """

    def __init__(self, radius=None):
        """
        Initialize the radius for shapes.
        :param radius: float, default None
        """
        self.radius = radius

    def calculate_circle_area(self):
        """
        Calculate the area of a circle based on the radius.
        :return: area of circle, float
        :raises ValueError: if radius is not initialized or is not a positive number
        """
        if self.radius is None or self.radius <= 0:
            raise ValueError("Radius must be a positive number and initialized.")
        return math.pi * self.radius**2

    def calculate_sphere_area(self):
        """
        Calculate the surface area of a sphere based on the radius.
        :return: area of sphere, float
        :raises ValueError: if radius is not initialized or is not a positive number
        """
        if self.radius is None or self.radius <= 0:
            raise ValueError("Radius must be a positive number and initialized.")
        return 4 * math.pi * self.radius**2

    def calculate_cylinder_area(self, height):
        """
        Calculate the surface area of a cylinder based on the radius and height.
        :param height: height of cylinder, float
        :return: area of cylinder, float
        :raises ValueError: if radius or height is not a positive number
        """
        if self.radius is None or self.radius <= 0:
            raise ValueError("Radius must be a positive number and initialized.")
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        return 2 * math.pi * self.radius * height + 2 * math.pi * self.radius**2

    def calculate_sector_area(self, angle):
        """
        Calculate the area of a sector based on the radius and angle.
        :param angle: angle of sector in radians, float
        :return: area of sector, float
        :raises ValueError: if radius is not a positive number or angle is not a positive number.
        """
        if self.radius is None or self.radius <= 0:
            raise ValueError("Radius must be a positive number and initialized.")
        if angle <= 0:
            raise ValueError("Angle must be a positive number.")
        return 0.5 * self.radius**2 * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        Calculate the area of an annulus based on the inner and outer radii.
        :param inner_radius: inner radius of annulus, float
        :param outer_radius: outer radius of annulus, float
        :return: area of annulus, float
        :raises ValueError: if inner_radius or outer_radius is not a positive number, or inner_radius is greater than or equal to outer_radius.
        """
        if inner_radius <= 0 or outer_radius <= 0:
            raise ValueError("Inner and outer radii must be positive numbers.")
        if inner_radius >= outer_radius:
            raise ValueError("Inner radius must be less than outer radius.")
        return math.pi * (outer_radius**2 - inner_radius**2)