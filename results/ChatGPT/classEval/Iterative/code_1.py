import math

class AreaCalculator:
    """
    This class calculates the area of various shapes, including a circle, sphere, cylinder, sector, and annulus.
    """

    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        :param radius: float, the radius of the shapes
        """
        if radius < 0:
            raise ValueError("Radius must be a non-negative value.")
        self.radius = radius

    def calculate_circle_area(self):
        """
        Calculate the area of a circle based on self.radius.
        :return: area of circle, float
        >>> area_calculator = AreaCalculator(2)
        >>> area_calculator.calculate_circle_area()
        12.566370614359172
        """
        return math.pi * self.radius ** 2

    def calculate_sphere_area(self):
        """
        Calculate the surface area of a sphere based on self.radius.
        :return: surface area of sphere, float
        >>> area_calculator = AreaCalculator(2)
        >>> area_calculator.calculate_sphere_area()
        50.26548245743669
        """
        return 4 * math.pi * self.radius ** 2

    def calculate_cylinder_area(self, height):
        """
        Calculate the surface area of a cylinder based on self.radius and height.
        :param height: float, height of the cylinder
        :return: surface area of cylinder, float
        >>> area_calculator = AreaCalculator(2)
        >>> area_calculator.calculate_cylinder_area(3)
        62.83185307179586
        """
        if height < 0:
            raise ValueError("Height must be a non-negative value.")
        return 2 * math.pi * self.radius * (self.radius + height)

    def calculate_sector_area(self, angle):
        """
        Calculate the area of a sector based on self.radius and angle in radians.
        :param angle: float, angle of the sector in radians
        :return: area of sector, float
        >>> area_calculator = AreaCalculator(2)
        >>> area_calculator.calculate_sector_area(math.pi)
        6.283185307179586
        """
        if angle < 0:
            raise ValueError("Angle must be a non-negative value.")
        return 0.5 * self.radius ** 2 * angle

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        Calculate the area of an annulus based on inner_radius and outer_radius.
        :param inner_radius: float, inner radius of the annulus
        :param outer_radius: float, outer radius of the annulus
        :return: area of annulus, float
        >>> area_calculator = AreaCalculator(2)
        >>> area_calculator.calculate_annulus_area(1, 3)
        12.566370614359172
        """
        if inner_radius < 0 or outer_radius < 0:
            raise ValueError("Both inner and outer radii must be non-negative values.")
        if inner_radius >= outer_radius:
            raise ValueError("Outer radius must be greater than inner radius.")
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)