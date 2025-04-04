from math import pi, fabs

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        return self.taylor(x, 10)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator = TriCalculator()
        >>> tricalculator.factorial(5)
        120
        """
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.taylor(60, 10)
        0.5000000000000001
        """
        radians = x * (pi / 180)
        cos_value = 0
        for i in range(n):
            term = ((-1) ** i) * (radians ** (2 * i)) / self.factorial(2 * i)
            cos_value += term
        return cos_value

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.sin(30)
        0.5
        """
        return self.taylor_sin(x, 10)

    def taylor_sin(self, x, n):
        """
        Finding the n-order Taylor expansion value of sin (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.taylor_sin(30, 10)
        0.49999999999999994
        """
        radians = x * (pi / 180)
        sin_value = 0
        for i in range(n):
            term = ((-1) ** i) * (radians ** (2 * i + 1)) / self.factorial(2 * i + 1)
            sin_value += term
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
        sin_value = self.sin(x)
        cos_value = self.cos(x)
        if fabs(cos_value) < 1e-10:
            raise ValueError("Tangent is undefined for angles where cosine is zero.")
        return sin_value / cos_value