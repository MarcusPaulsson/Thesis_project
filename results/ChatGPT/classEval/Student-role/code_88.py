from math import pi, fabs

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    def cos(self, x):
        """Calculate the cos value of the x-degree angle"""
        return self.taylor(x, 50)

    def factorial(self, a):
        """Calculate the factorial of a"""
        if a == 0:
            return 1
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    def taylor(self, x, n):
        """Finding the n-order Taylor expansion value of cos (x/180 * pi)"""
        x_rad = x * (pi / 180)
        cos_value = 0
        for i in range(n):
            cos_value += ((-1) ** i) * (x_rad ** (2 * i)) / self.factorial(2 * i)
        return cos_value

    def sin(self, x):
        """Calculate the sin value of the x-degree angle"""
        x_rad = x * (pi / 180)
        sin_value = 0
        for i in range(50):
            sin_value += ((-1) ** i) * (x_rad ** (2 * i + 1)) / self.factorial(2 * i + 1)
        return sin_value

    def tan(self, x):
        """Calculate the tan value of the x-degree angle"""
        cos_value = self.cos(x)
        if fabs(cos_value) < 1e-10:  # Prevent division by zero
            return False
        return self.sin(x) / cos_value