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

# Unit tests
import unittest

class AreaCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.circle_calculator = AreaCalculator(2)
        self.sphere_calculator = AreaCalculator(2)
        self.cylinder_calculator = AreaCalculator(2)
        self.annulus_calculator = AreaCalculator(2.5)

    def test_calculate_circle_area(self):
        self.assertAlmostEqual(12.57, self.circle_calculator.calculate_circle_area(), delta=0.01)

    def test_calculate_sphere_area(self):
        self.assertAlmostEqual(50.27, self.sphere_calculator.calculate_sphere_area(), delta=0.01)

    def test_calculate_cylinder_area(self):
        self.assertAlmostEqual(50.27, self.cylinder_calculator.calculate_cylinder_area(2), delta=0.01)

    def test_calculate_sector_area(self):
        self.assertAlmostEqual(6.28, self.circle_calculator.calculate_sector_area(math.pi), delta=0.01)

    def test_calculate_annulus_area(self):
        self.assertAlmostEqual(25.13, self.annulus_calculator.calculate_annulus_area(1, 3), delta=0.01)

if __name__ == "__main__":
    unittest.main()