from math import pi

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cosine value of the x-degree angle.
        :param x: float
        :return: float
        """
        return self._taylor_cos(x, 50)

    def factorial(self, n):
        """
        Calculate the factorial of n.
        :param n: int
        :return: int
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def _taylor_cos(self, x, n):
        """
        Calculate the n-order Taylor expansion value of cos(x) where x is in radians.
        :param x: float
        :param n: int
        :return: float
        """
        radians = x * (pi / 180)
        cos_value = sum(((-1) ** i) * (radians ** (2 * i)) / self.factorial(2 * i) for i in range(n))
        return cos_value

    def sin(self, x):
        """
        Calculate the sine value of the x-degree angle.
        :param x: float
        :return: float
        """
        return self._taylor_sin(x, 50)

    def _taylor_sin(self, x, n):
        """
        Calculate the n-order Taylor expansion value of sin(x) where x is in radians.
        :param x: float
        :param n: int
        :return: float
        """
        radians = x * (pi / 180)
        sin_value = sum(((-1) ** i) * (radians ** (2 * i + 1)) / self.factorial(2 * i + 1) for i in range(n))
        return sin_value

    def tan(self, x):
        """
        Calculate the tangent value of the x-degree angle.
        :param x: float
        :return: float or bool
        """
        if x % 180 == 90:
            return False  # Undefined for odd multiples of 90 degrees
        return self.sin(x) / self.cos(x)