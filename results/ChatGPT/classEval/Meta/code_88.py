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
        radians = x * (pi / 180)
        return self.taylor(radians, 50)

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
        result = 0
        for i in range(n):
            term = ((-1) ** i) * (x ** (2 * i)) / self.factorial(2 * i)
            result += term
        return result

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        """
        radians = x * (pi / 180)
        return self.taylor_sin(radians, 50)

    def taylor_sin(self, x, n):
        """
        Finding the n-order Taylor expansion value of sin (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        result = 0
        for i in range(n):
            term = ((-1) ** i) * (x ** (2 * i + 1)) / self.factorial(2 * i + 1)
            result += term
        return result

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        """
        cos_value = self.cos(x)
        if cos_value == 0:
            return False
        return self.sin(x) / cos_value