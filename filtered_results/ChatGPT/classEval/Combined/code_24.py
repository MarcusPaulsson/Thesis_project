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
        :raises ValueError: If the second complex number is zero.
        """
        if c2 == 0:
            raise ValueError("Cannot divide by zero.")
        return c1 / c2