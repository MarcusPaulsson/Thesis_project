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
        x = x % 360
        radians = x * pi / 180
        result = self.taylor(x, 50)
        return result

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        """
        if a == 0:
            return 1
        else:
            fact = 1
            for i in range(1, a + 1):
                fact = fact * i
            return fact

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        x = x % 360
        x = x * pi / 180
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
        x = x % 360
        radians = x * pi / 180
        sin_approx = 0
        n = 50
        for i in range(n):
            numerator = (-1)**i * (radians)**(2*i + 1)
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
          cos_val = self.cos(x)
          if cos_val == 0:
            return False
          return self.sin(x) / cos_val