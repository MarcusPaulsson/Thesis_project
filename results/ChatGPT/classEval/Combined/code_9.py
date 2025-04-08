class BigNumCalculator:
    """
    A class that implements big number calculations, including addition, subtraction, and multiplication.
    """

    @staticmethod
    def add(num1: str, num2: str) -> str:
        """
        Adds two big numbers.
        :param num1: The first number to add, str.
        :param num2: The second number to add, str.
        :return: The sum of the two numbers, str.
        """
        return str(int(num1) + int(num2))

    @staticmethod
    def subtract(num1: str, num2: str) -> str:
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract, str.
        :param num2: The second number to subtract, str.
        :return: The difference of the two numbers, str.
        """
        return str(int(num1) - int(num2))

    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply, str.
        :param num2: The second number to multiply, str.
        :return: The product of the two numbers, str.
        """
        return str(int(num1) * int(num2))


import unittest

class BigNumCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = BigNumCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add("12345678901234567890", "98765432109876543210"), "111111111011111111100")
        self.assertEqual(self.calculator.add("123456789012345678922", "98765432109876543210"), "222222221122222222132")
        self.assertEqual(self.calculator.add("123456789012345678934", "98765432109876543210"), "222222221122222222144")
        self.assertEqual(self.calculator.add("123456789012345678946", "98765432109876543210"), "222222221122222222156")
        self.assertEqual(self.calculator.add("123456789012345678958", "98765432109876543210"), "222222221122222222168")

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract("12345678901234567890", "98765432109876543210"), "-86419753208641975320")
        self.assertEqual(self.calculator.subtract("123456789012345678922", "98765432109876543210"), "24691356902469135712")
        self.assertEqual(self.calculator.subtract("123456789012345678934", "98765432109876543"), "123358023580235802391")
        self.assertEqual(self.calculator.subtract("12345678901234567", "98765432109876543210"), "-98753086430975308643")
        self.assertEqual(self.calculator.subtract("923456789", "187654321"), "735802468")

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply("12345678901234567890", "98765432109876543210"), "1219326311370217952237463801111263526900")
        self.assertEqual(self.calculator.multiply("123456789012345678922", "98765432109876543210"), "12193263113702179524547477517529919219620")
        self.assertEqual(self.calculator.multiply("123456789012345678934", "98765432109876543"), "12193263113702179499806737010255845162")
        self.assertEqual(self.calculator.multiply("12345678901234567", "98765432109876543210"), "1219326311370217864336229223321140070")
        self.assertEqual(self.calculator.multiply("923456789", "187654321"), "173290656712635269")
        self.assertEqual(self.calculator.multiply("000000001", "000000001"), "1")

    def test_main(self):
        self.assertEqual(self.calculator.add("12345678901234567890", "98765432109876543210"), "111111111011111111100")
        self.assertEqual(self.calculator.subtract("12345678901234567890", "98765432109876543210"), "-86419753208641975320")
        self.assertEqual(self.calculator.multiply("12345678901234567890", "98765432109876543210"), "1219326311370217952237463801111263526900")

if __name__ == '__main__':
    unittest.main()