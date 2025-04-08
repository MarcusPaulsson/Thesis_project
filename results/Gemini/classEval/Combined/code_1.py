import math

class AreaCalculator:
    """
    This is a class for calculating the area of different shapes.
    """

    def __init__(self, radius):
        """
        Initializes the AreaCalculator with a radius.

        :param radius: The radius to be used in calculations.
        :raises TypeError: if radius is not a number.
        :raises ValueError: if radius is negative.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = float(radius)

    def calculate_circle_area(self):
        """
        Calculates the area of a circle.

        :return: The area of the circle.
        :rtype: float
        """
        return math.pi * self.radius**2

    def calculate_sphere_area(self):
        """
        Calculates the surface area of a sphere.

        :return: The surface area of the sphere.
        :rtype: float
        """
        return 4 * math.pi * self.radius**2

    def calculate_cylinder_area(self, height):
        """
        Calculates the surface area of a cylinder.

        :param height: The height of the cylinder.
        :type height: float
        :raises TypeError: if height is not a number.
        :raises ValueError: if height is negative.
        :return: The surface area of the cylinder.
        :rtype: float
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number.")
        if height < 0:
            raise ValueError("Height cannot be negative.")

        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        """
        Calculates the area of a sector of a circle.

        :param angle: The angle of the sector in radians.
        :type angle: float
        :raises TypeError: if angle is not a number.
        :return: The area of the sector.
        :rtype: float
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a number.")

        return 0.5 * self.radius**2 * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        Calculates the area of an annulus (ring).

        :param inner_radius: The inner radius of the annulus.
        :type inner_radius: float
        :param outer_radius: The outer radius of the annulus.
        :type outer_radius: float
        :raises TypeError: if inner_radius or outer_radius are not numbers.
        :raises ValueError: if inner_radius or outer_radius are negative, or if inner_radius >= outer_radius.
        :return: The area of the annulus.
        :rtype: float
        """
        if not isinstance(inner_radius, (int, float)) or not isinstance(outer_radius, (int, float)):
            raise TypeError("Inner and outer radii must be numbers.")

        if inner_radius < 0 or outer_radius < 0:
            raise ValueError("Radii cannot be negative.")

        if inner_radius >= outer_radius:
            raise ValueError("Inner radius must be smaller than outer radius.")

        return math.pi * (outer_radius**2 - inner_radius**2)