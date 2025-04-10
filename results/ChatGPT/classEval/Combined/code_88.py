from math import pi

class TriCalculator:
    """
    The class allows calculating trigonometric values, including cosine, sine, and tangent,
    using Taylor series approximations.
    """

    def factorial(self, a: int) -> int:
        """
        Calculate the factorial of a non-negative integer.
        :param a: int - non-negative integer
        :return: int - factorial of a
        """
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result

    def taylor_cos(self, x: float, n: int) -> float:
        """
        Calculate the n-order Taylor expansion value of cos(x) where x is in radians.
        :param x: float - angle in radians
        :param n: int - number of terms in the Taylor series
        :return: float - cosine of x
        """
        cos_value = 0
        for i in range(n):
            term = ((-1) ** i) * (x ** (2 * i)) / self.factorial(2 * i)
            cos_value += term
        return cos_value

    def taylor_sin(self, x: float, n: int) -> float:
        """
        Calculate the n-order Taylor expansion value of sin(x) where x is in radians.
        :param x: float - angle in radians
        :param n: int - number of terms in the Taylor series
        :return: float - sine of x
        """
        sin_value = 0
        for i in range(n):
            term = ((-1) ** i) * (x ** (2 * i + 1)) / self.factorial(2 * i + 1)
            sin_value += term
        return sin_value

    def cos(self, x: float) -> float:
        """
        Calculate the cosine value of the x-degree angle.
        :param x: float - angle in degrees
        :return: float - cosine of x
        """
        radians = x * (pi / 180)
        return self.taylor_cos(radians, 50)

    def sin(self, x: float) -> float:
        """
        Calculate the sine value of the x-degree angle.
        :param x: float - angle in degrees
        :return: float - sine of x
        """
        radians = x * (pi / 180)
        return self.taylor_sin(radians, 50)

    def tan(self, x: float) -> float:
        """
        Calculate the tangent value of the x-degree angle.
        :param x: float - angle in degrees
        :return: float or bool - tangent of x or False if undefined
        """
        if x % 180 == 90:
            return False  # Undefined value for tangent
        return self.sin(x) / self.cos(x)