from math import pi



class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self, taylor_order=50):
        """
        Initializes the TriCalculator with a default Taylor series order.
        :param taylor_order: int, the order of the Taylor series approximation.  Defaults to 50.
        """
        self.taylor_order = taylor_order

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

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: float
        :param n: int
        :return: float
        """
        x_rad = x * pi / 180
        cos_approx = 0
        for i in range(n):
            numerator = x_rad ** (2 * i)
            denominator = self.factorial(2 * i)
            term = (-1) ** i * (numerator / denominator)
            cos_approx += term
        return cos_approx

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle using Taylor series.
        :param x: float
        :return: float
        """
        return self.taylor(x, self.taylor_order)

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle using Taylor series.
        :param x: float
        :return: float
        """
        x_rad = x * pi / 180
        sin_approx = 0
        for n in range(self.taylor_order):
            term = ((-1) ** n) * (x_rad ** (2 * n + 1)) / self.factorial(2 * n + 1)
            sin_approx += term
        return sin_approx

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle.
        :param x: float
        :return: float or False if cos(x) is 0
        """
        if x % 180 == 90:
            return False

        cos_x = self.cos(x)
        if abs(cos_x) < 1e-15:  # Using a small tolerance for floating-point comparison
            return False
        sin_x = self.sin(x)
        return sin_x / cos_x

