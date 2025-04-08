from math import pi
import unittest


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


class TriCalculatorTestCos(unittest.TestCase):
    def test_cos_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(60), 0.5, places=9)

    def test_cos_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(30), 0.8660254038, places=9)

    def test_cos_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(0), 1.0, places=9)

    def test_cos_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(90), 0.0, places=9)

    def test_cos_5(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(45), 0.7071067812, places=9)


class TriCalculatorTestFactorial(unittest.TestCase):
    def test_factorial_1(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(5), 120)

    def test_factorial_2(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(4), 24)

    def test_factorial_3(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(3), 6)

    def test_factorial_4(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(2), 2)

    def test_factorial_5(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(1), 1)

    def test_factorial_6(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(0), 1)

    def test_factorial_invalid_input(self):
        tricalculator = TriCalculator()
        with self.assertRaises(TypeError):
            tricalculator.factorial(1.5)
        with self.assertRaises(ValueError):
            tricalculator.factorial(-1)


class TriCalculatorTestTaylor(unittest.TestCase):
    def test_taylor_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(60, 50), 0.5, places=9)

    def test_taylor_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(30, 50), 0.8660254037844386, places=9)

    def test_taylor_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(90, 50), 0.0, places=9)

    def test_taylor_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(0, 50), 1.0, places=9)

    def test_taylor_5(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(45, 50), 0.7071067811865475, places=9)


class TriCalculatorTestSin(unittest.TestCase):
    def test_sin_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(30), 0.5, places=9)

    def test_sin_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(60), 0.8660254038, places=9)

    def test_sin_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(0), 0.0, places=9)

    def test_sin_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(90), 1.0, places=9)

    def test_sin_5(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(45), 0.7071067812, places=9)


class TriCalculatorTestTan(unittest.TestCase):
    def test_tan_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(45), 1.0, places=9)

    def test_tan_2(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.tan(90), False)

    def test_tan_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(30), 0.5773502692, places=9)

    def test_tan_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(60), 1.7320508076, places=9)

    def test_tan_5(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(0), 0.0, places=9)


class TriCalculatorTest(unittest.TestCase):
    def test_tricalculator(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(60), 0.5, places=9)
        self.assertAlmostEqual(tricalculator.taylor(60, 50), 0.5, places=9)
        self.assertAlmostEqual(tricalculator.sin(30), 0.5, places=9)
        self.assertAlmostEqual(tricalculator.tan(45), 1.0, places=9)
        self.assertEqual(tricalculator.tan(90), False)