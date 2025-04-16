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
        x_rad = x / 180 * pi
        return self.taylor_cos(x_rad, 15)

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
            return a * self.factorial(a-1)

    def taylor_cos(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x)
        :param x: float
        :param n: int
        :return: float
        >>> tricalculator.taylor_cos(60, 50)
        0.5000000000000001
        """
        result = 0
        for i in range(n):
            term = ((-1)**i) * (x**(2*i)) / self.factorial(2*i)
            result += term
        return result

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        x_rad = x / 180 * pi
        result = 0
        for i in range(10):
            term = ((-1)**i) * (x_rad**(2*i+1)) / self.factorial(2*i+1)
            result += term
        return result


    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        if x == 90:
            return False
        x_rad = x / 180 * pi
        return self.sin(x) / self.cos(x)