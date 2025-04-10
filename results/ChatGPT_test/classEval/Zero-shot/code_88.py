from math import pi

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
        return self.taylor(x, 50)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        """
        if a == 0 or a == 1:
            return 1
        return a * self.factorial(a - 1)

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        x_rad = x * (pi / 180)
        cos_value = 0
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
        return self.taylor_sin(x, 50)

    def taylor_sin(self, x, n):
        """
        Finding the n-order Taylor expansion value of sin (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        x_rad = x * (pi / 180)
        sin_value = 0
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
        if x % 180 == 90:
            return False  # Undefined for odd multiples of 90 degrees
        return self.sin(x) / self.cos(x)