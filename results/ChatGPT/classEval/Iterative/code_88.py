from math import pi, factorial as math_factorial, fabs

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
        """
        return self.taylor(x, 50)  # 50 terms for approximation

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        """
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return 1 if a == 0 else math_factorial(a)

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        x_rad = x * (pi / 180)  # Convert degrees to radians
        cos_value = 0.0
        for i in range(n):
            term = ((-1) ** i) * (x_rad ** (2 * i)) / self.factorial(2 * i)
            cos_value += term
        return cos_value

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        """
        return self.taylor_sine(x, 50)  # 50 terms for approximation

    def taylor_sine(self, x, n):
        """
        Finding the n-order Taylor expansion value of sin (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        x_rad = x * (pi / 180)  # Convert degrees to radians
        sin_value = 0.0
        for i in range(n):
            term = ((-1) ** i) * (x_rad ** (2 * i + 1)) / self.factorial(2 * i + 1)
            sin_value += term
        return sin_value

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        """
        sin_value = self.sin(x)
        cos_value = self.cos(x)
        if fabs(cos_value) < 1e-10:  # Check for division by zero
            return False
        return sin_value / cos_value