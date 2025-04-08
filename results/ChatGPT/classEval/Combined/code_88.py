from math import pi

class TriCalculator:
    """
    The class allows calculating trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle.
        :param x: float
        :return: float
        """
        return self._taylor_series(x, 50, is_cos=True)

    def factorial(self, n):
        """
        Calculate the factorial of n.
        :param n: int
        :return: int
        :raises ValueError: If n is negative.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def _taylor_series(self, x, n, is_cos=False):
        """
        Calculate the n-order Taylor series expansion for cosine or sine.
        :param x: int
        :param n: int
        :param is_cos: bool, True for cosine, False for sine
        :return: float
        """
        radians = x * (pi / 180)
        series_value = 0
        for i in range(n):
            if is_cos:
                term = ((-1) ** i) * (radians ** (2 * i)) / self.factorial(2 * i)
            else:
                term = ((-1) ** i) * (radians ** (2 * i + 1)) / self.factorial(2 * i + 1)
            series_value += term
        return series_value

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle.
        :param x: float
        :return: float
        """
        return self._taylor_series(x, 50, is_cos=False)

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle.
        :param x: float
        :return: float or bool, False if tangent is undefined
        """
        if x % 180 == 90:
            return False  # tan is undefined for 90 + k*180 degrees
        return self.sin(x) / self.cos(x)