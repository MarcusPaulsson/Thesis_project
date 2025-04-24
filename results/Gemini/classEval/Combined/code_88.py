from math import pi
import unittest

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        self.n_terms = 50  # Default number of Taylor series terms

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        """
        if not isinstance(a, int):
            raise TypeError("Input must be an integer.")
        if a < 0:
            raise ValueError("Input must be a non-negative integer.")

        if a == 0:
            return 1
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    def taylor_cos(self, x, n):
        """
        Calculate the n-order Taylor expansion value of cos(x) in radians.
        :param x: float (in radians)
        :param n: int
        :return: float
        """
        result = 0.0
        for i in range(n):
            numerator = (-1)**i * x**(2*i)
            denominator = self.factorial(2*i)
            result += numerator / denominator
        return result

    def taylor_sin(self, x, n):
        """
        Calculate the n-order Taylor expansion value of sin(x) in radians.
        :param x: float (in radians)
        :param n: int
        :return: float
        """
        result = 0.0
        for i in range(n):
            numerator = (-1)**i * x**(2*i + 1)
            denominator = self.factorial(2*i + 1)
            result += numerator / denominator
        return result

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle using Taylor series.
        :param x: float (in degrees)
        :return: float
        """
        x_rad = x * pi / 180.0
        return self.taylor_cos(x_rad, self.n_terms)

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle using Taylor series.
        :param x: float (in degrees)
        :return: float
        """
        x_rad = x * pi / 180.0
        return self.taylor_sin(x_rad, self.n_terms)

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle using Taylor series.
        :param x: float (in degrees)
        :return: float or bool
        """
        if x % 180 == 90:
            return False  # Or raise an exception: raise ValueError("Tangent is undefined at x = 90 + 180k degrees")
        else:
            cos_x = self.cos(x)
            if cos_x == 0:
                return False
            return self.sin(x) / cos_x