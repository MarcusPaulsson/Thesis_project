from math import pi, fabs

class TriCalculator:
    """
    Calculates trigonometric values (cosine, sine, tangent) using Taylor series approximations.
    """

    def __init__(self, taylor_terms=50):
        """
        Initializes the TriCalculator with the number of Taylor series terms to use.

        Args:
            taylor_terms (int): The number of terms to use in the Taylor series approximation.
                                 Higher values provide better accuracy but increase computation time.
                                 Defaults to 50.
        """
        self.taylor_terms = taylor_terms

    def _factorial(self, a):
        """
        Calculates the factorial of a non-negative integer.

        Args:
            a (int): A non-negative integer.

        Returns:
            int: The factorial of a.  Returns 1 if a is 0.

        Raises:
            ValueError: If a is negative.
        """
        if not isinstance(a, int):
            raise TypeError("Factorial input must be an integer.")
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if a == 0:
            return 1
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    def _taylor_cos(self, x_rad, n):
        """
        Calculates the n-order Taylor series expansion value of cos(x_rad).

        Args:
            x_rad (float): The angle in radians.
            n (int): The number of terms to use in the Taylor series.

        Returns:
            float: The approximate cosine value.
        """
        cos_approx = 0
        for i in range(n):
            numerator = x_rad**(2*i)
            denominator = self._factorial(2*i)
            cos_approx += ((-1)**i) * (numerator/denominator)
        return cos_approx

    def _taylor_sin(self, x_rad, n):
        """
        Calculates the n-order Taylor series expansion value of sin(x_rad).

        Args:
            x_rad (float): The angle in radians.
            n (int): The number of terms to use in the Taylor series.

        Returns:
            float: The approximate sine value.
        """
        sin_approx = 0
        for i in range(n):
            numerator = x_rad**(2*i+1)
            denominator = self._factorial(2*i+1)
            sin_approx += ((-1)**i) * (numerator/denominator)
        return sin_approx

    def cos(self, x_deg):
        """
        Calculates the cosine of an angle given in degrees using the Taylor series approximation.

        Args:
            x_deg (float): The angle in degrees.

        Returns:
            float: The approximate cosine value.
        """
        x_rad = (x_deg / 180) * pi
        return self._taylor_cos(x_rad, self.taylor_terms)

    def sin(self, x_deg):
        """
        Calculates the sine of an angle given in degrees using the Taylor series approximation.

        Args:
            x_deg (float): The angle in degrees.

        Returns:
            float: The approximate sine value.
        """
        x_rad = (x_deg / 180) * pi
        return self._taylor_sin(x_rad, self.taylor_terms)

    def tan(self, x_deg):
        """
        Calculates the tangent of an angle given in degrees using the Taylor series approximation.

        Args:
            x_deg (float): The angle in degrees.

        Returns:
            float: The approximate tangent value.  Returns infinity if cosine is close to zero.
        """
        cos_val = self.cos(x_deg)
        if fabs(cos_val) < 1e-10:  # Check if cosine is close to zero to avoid division by zero
            return float('inf')  # Return infinity if cosine is zero
        return self.sin(x_deg) / cos_val