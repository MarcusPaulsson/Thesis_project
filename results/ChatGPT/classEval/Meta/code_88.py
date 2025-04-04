from math import pi

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator = TriCalculator()
        >>> tricalculator.factorial(5)
        120
        """
        if a == 0 or a == 1:
            return 1
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        x_rad = x * (pi / 180)  # Convert degrees to radians
        cos_value = 0
        for i in range(n):
            sign = (-1) ** i
            cos_value += sign * (x_rad ** (2 * i)) / self.factorial(2 * i)
        return cos_value

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        return self.taylor(x, 50)

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.sin(30)
        0.5
        """
        x_rad = x * (pi / 180)  # Convert degrees to radians
        sin_value = 0
        for i in range(50):
            sign = (-1) ** i
            sin_value += sign * (x_rad ** (2 * i + 1)) / self.factorial(2 * i + 1)
        return sin_value

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.tan(45)
        1.0
        """
        return self.sin(x) / self.cos(x)