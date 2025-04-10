class ComplexCalculator:
    """
    A class that implements addition, subtraction, multiplication, and division operations for complex numbers.
    """

    @staticmethod
    def add(c1: complex, c2: complex) -> complex:
        """
        Adds two complex numbers.
        
        :param c1: The first complex number.
        :param c2: The second complex number.
        :return: The sum of the two complex numbers.
        """
        return c1 + c2

    @staticmethod
    def subtract(c1: complex, c2: complex) -> complex:
        """
        Subtracts two complex numbers.
        
        :param c1: The first complex number.
        :param c2: The second complex number.
        :return: The difference of the two complex numbers.
        """
        return c1 - c2

    @staticmethod
    def multiply(c1: complex, c2: complex) -> complex:
        """
        Multiplies two complex numbers.
        
        :param c1: The first complex number.
        :param c2: The second complex number.
        :return: The product of the two complex numbers.
        """
        return c1 * c2

    @staticmethod
    def divide(c1: complex, c2: complex) -> complex:
        """
        Divides two complex numbers.
        
        :param c1: The first complex number.
        :param c2: The second complex number.
        :return: The quotient of the two complex numbers.
        :raises ValueError: If attempting to divide by zero.
        """
        if c2 == 0:
            raise ValueError("Cannot divide by zero.")
        return c1 / c2


# Unit tests for ComplexCalculator
import unittest

class ComplexCalculatorTestAdd(unittest.TestCase):
    def test_add(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.add(1+2j, 3+4j), (4+6j))

    def test_add_negative(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.add(-1-2j, -3-4j), (-4-6j))

    def test_add_mixed(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.add(1-2j, 3-4j), (4-6j))

    def test_add_mixed_signs(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.add(-1+2j, -3+4j), (-4+6j))

    def test_add_inverse(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.add(1+2j, -1-2j), (0+0j))


class ComplexCalculatorTestSubtract(unittest.TestCase):
    def test_subtract(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.subtract(1+2j, 3+4j), (-2-2j))

    def test_subtract_negative(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.subtract(-1-2j, -3-4j), (2+2j))

    def test_subtract_mixed(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.subtract(1-2j, 3-4j), (-2+2j))

    def test_subtract_mixed_signs(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.subtract(-1+2j, -3+4j), (2-2j))

    def test_subtract_zero(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.subtract(1+2j, 1+2j), (0+0j))


class ComplexCalculatorTestMultiply(unittest.TestCase):
    def test_multiply(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.multiply(1+2j, 3+4j), (-5+10j))

    def test_multiply_negative(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.multiply(-1-2j, -3-4j), (-5+10j))

    def test_multiply_mixed(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.multiply(1-2j, 3-4j), (-5-10j))

    def test_multiply_mixed_signs(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.multiply(-1+2j, -3+4j), (-5-10j))

    def test_multiply_inverse(self):
        calculator = ComplexCalculator()
        self.assertEqual(calculator.multiply(1+2j, -1-2j), (3-4j))


class ComplexCalculatorTestDivide(unittest.TestCase):
    def test_divide(self):
        calculator = ComplexCalculator()
        self.assertAlmostEqual(calculator.divide(1+2j, 3+4j), (0.44+0.08j), places=2)

    def test_divide_negative(self):
        calculator = ComplexCalculator()
        self.assertAlmostEqual(calculator.divide(-1-2j, -3-4j), (0.44+0.08j), places=2)

    def test_divide_mixed(self):
        calculator = ComplexCalculator()
        self.assertAlmostEqual(calculator.divide(1-2j, 3-4j), (0.44-0.08j), places=2)

    def test_divide_mixed_signs(self):
        calculator = ComplexCalculator()
        self.assertAlmostEqual(calculator.divide(-1+2j, -3+4j), (0.44-0.08j), places=2)

    def test_divide_inverse(self):
        calculator = ComplexCalculator()
        self.assertAlmostEqual(calculator.divide(1+2j, -1-2j), (-1+0j), places=2)

    def test_divide_by_zero(self):
        calculator = ComplexCalculator()
        with self.assertRaises(ValueError):
            calculator.divide(1+2j, 0)


if __name__ == '__main__':
    unittest.main()