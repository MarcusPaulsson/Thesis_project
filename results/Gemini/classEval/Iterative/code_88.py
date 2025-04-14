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
        :param x:float
        :return:float
        """
        return self.taylor(x, 50)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        """
        if not isinstance(a, int):
            raise TypeError("Factorial input must be an integer.")
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if a == 0:
            return 1
        else:
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
        """
        x = x / 180 * pi
        cos_approx = 0
        for i in range(n):
            numerator = (-1)**i * x**(2*i)
            denominator = self.factorial(2*i)
            cos_approx += numerator / denominator
        return cos_approx

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        """
        x = x / 180 * pi
        sin_approx = 0
        for i in range(50):
            numerator = (-1)**i * x**(2*i + 1)
            denominator = self.factorial(2*i + 1)
            sin_approx += numerator / denominator
        return sin_approx


    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        """
        if x % 180 == 90:
            return False
        else:
            cos_x = self.cos(x)
            if cos_x == 0:
                return False
            return self.sin(x) / cos_x