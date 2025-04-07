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
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        return self.taylor(x, 50)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
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
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        x = x / 180 * pi
        cos_value = 0
        for i in range(n):
            numerator = (-1) ** i * x ** (2 * i)
            denominator = self.factorial(2 * i)
            cos_value += numerator / denominator
        return cos_value

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        x = x / 180 * pi
        sin_value = 0
        for i in range(50):
            numerator = (-1) ** i * x ** (2 * i + 1)
            denominator = self.factorial(2 * i + 1)
            sin_value += numerator / denominator
        return sin_value


    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        if x % 180 == 90:
            return False
        else:
            return self.sin(x) / self.cos(x)