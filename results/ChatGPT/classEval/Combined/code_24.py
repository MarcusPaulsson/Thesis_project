class ComplexCalculator:
    """
    A calculator for performing basic operations on complex numbers.
    """

    @staticmethod
    def add(c1, c2):
        """Adds two complex numbers."""
        return c1 + c2

    @staticmethod
    def subtract(c1, c2):
        """Subtracts the second complex number from the first."""
        return c1 - c2

    @staticmethod
    def multiply(c1, c2):
        """Multiplies two complex numbers."""
        return c1 * c2

    @staticmethod
    def divide(c1, c2):
        """Divides the first complex number by the second."""
        if c2 == 0:
            raise ValueError("Cannot divide by zero.")
        return c1 / c2


# Test cases
import unittest

class TestComplexCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ComplexCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1+2j, 3+4j), (4+6j))
        self.assertEqual(self.calculator.add(-1 - 2j, -3 - 4j), (-4 - 6j))
        self.assertEqual(self.calculator.add(1-2j, 3-4j), (4-6j))
        self.assertEqual(self.calculator.add(-1+2j, -3+4j), (-4+6j))
        self.assertEqual(self.calculator.add(1+2j, -1-2j), (0+0j))

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(1+2j, 3+4j), (-2-2j))
        self.assertEqual(self.calculator.subtract(-1-2j, -3-4j), (2+2j))
        self.assertEqual(self.calculator.subtract(1-2j, 3-4j), (-2+2j))
        self.assertEqual(self.calculator.subtract(-1+2j, -3+4j), (2-2j))
        self.assertEqual(self.calculator.subtract(1+2j, 1+2j), (0+0j))

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(1+2j, 3+4j), (-5+10j))
        self.assertEqual(self.calculator.multiply(-1-2j, -3-4j), (-5+10j))
        self.assertEqual(self.calculator.multiply(1-2j, 3-4j), (-5-10j))
        self.assertEqual(self.calculator.multiply(-1+2j, -3+4j), (-5-10j))
        self.assertEqual(self.calculator.multiply(1+2j, -1-2j), (3-4j))

    def test_divide(self):
        self.assertAlmostEqual(self.calculator.divide(1+2j, 3+4j), (0.44+0.08j), places=2)
        self.assertAlmostEqual(self.calculator.divide(-1-2j, -3-4j), (0.44+0.08j), places=2)
        self.assertAlmostEqual(self.calculator.divide(1-2j, 3-4j), (0.44-0.08j), places=2)
        self.assertAlmostEqual(self.calculator.divide(-1+2j, -3+4j), (0.44-0.08j), places=2)
        self.assertEqual(self.calculator.divide(1+2j, -1-2j), (-1+0j))

if __name__ == "__main__":
    unittest.main()