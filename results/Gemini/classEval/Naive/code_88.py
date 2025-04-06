from math import pi, fabs

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self, tolerance=1e-15):
        """
        Initializes the TriCalculator with a specified tolerance for Taylor series approximations.

        :param tolerance: float, the acceptable error for the Taylor series calculation. Defaults to 1e-15.
        """
        self.tolerance = tolerance

    def cos(self, x):
        """
        Calculate the cosine value of the x-degree angle using Taylor series approximation.

        :param x: float, angle in degrees
        :return: float, cosine of the angle
        """
        return self.taylor_cos(x, tolerance=self.tolerance)

    def factorial(self, a):
        """
        Calculate the factorial of a non-negative integer a.

        :param a: int, non-negative integer
        :return: int, factorial of a
        :raises ValueError: if a is negative
        """
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if a == 0:
            return 1
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    def taylor_cos(self, x, n_terms=50, tolerance=1e-15):
        """
        Calculate the cosine of x (in degrees) using the Taylor series expansion.

        :param x: float, angle in degrees
        :param n_terms: int, maximum number of terms to use in the Taylor series. Defaults to 50.
        :param tolerance: float, acceptable error for the Taylor series calculation. Defaults to 1e-15.
        :return: float, cosine of x calculated using the Taylor series
        """
        x_radians = x * pi / 180.0
        result = 0.0
        term = 1.0
        i = 0
        while fabs(term) > tolerance and i < n_terms:
            result += term
            i += 2
            term *= - (x_radians ** 2) / (i * (i - 1))
        return result

    def sin(self, x):
        """
        Calculate the sine value of the x-degree angle using Taylor series approximation.

        :param x: float, angle in degrees
        :return: float, sine of the angle
        """
        return self.taylor_sin(x, tolerance=self.tolerance)

    def taylor_sin(self, x, n_terms=50, tolerance=1e-15):
        """
        Calculate the sine of x (in degrees) using the Taylor series expansion.

        :param x: float, angle in degrees
        :param n_terms: int, maximum number of terms to use in the Taylor series. Defaults to 50.
        :param tolerance: float, acceptable error for the Taylor series calculation. Defaults to 1e-15.
        :return: float, sine of x calculated using the Taylor series
        """
        x_radians = x * pi / 180.0
        result = 0.0
        term = x_radians
        i = 1
        while fabs(term) > tolerance and i < n_terms:
            result += term
            i += 2
            term *= - (x_radians ** 2) / (i * (i - 1))
        return result

    def tan(self, x):
        """
        Calculate the tangent value of the x-degree angle.

        :param x: float, angle in degrees
        :return: float, tangent of the angle
        :raises ZeroDivisionError: if cos(x) is close to zero.
        """
        cos_x = self.cos(x)
        if fabs(cos_x) < self.tolerance:
            raise ZeroDivisionError("Tangent is undefined at this angle (cosine is zero).")
        return self.sin(x) / cos_x

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        return self.taylor_cos(x, n_terms=n)