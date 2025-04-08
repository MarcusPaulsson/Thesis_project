class ComplexCalculator:
    """
    This is a class that implements addition, subtraction, multiplication, and division operations for complex numbers.
    """

    def __init__(self):
        pass

    @staticmethod
    def add(c1: complex, c2: complex) -> complex:
        """
        Adds two complex numbers.

        Args:
            c1: The first complex number.
            c2: The second complex number.

        Returns:
            The sum of the two complex numbers.

        Examples:
            >>> ComplexCalculator.add(1+2j, 3+4j)
            (4+6j)
        """
        return c1 + c2

    @staticmethod
    def subtract(c1: complex, c2: complex) -> complex:
        """
        Subtracts two complex numbers.

        Args:
            c1: The first complex number.
            c2: The second complex number.

        Returns:
            The difference of the two complex numbers.

        Examples:
            >>> ComplexCalculator.subtract(1+2j, 3+4j)
            (-2-2j)
        """
        return c1 - c2

    @staticmethod
    def multiply(c1: complex, c2: complex) -> complex:
        """
        Multiplies two complex numbers.

        Args:
            c1: The first complex number.
            c2: The second complex number.

        Returns:
            The product of the two complex numbers.

        Examples:
            >>> ComplexCalculator.multiply(1+2j, 3+4j)
            (-5+10j)
        """
        return c1 * c2

    @staticmethod
    def divide(c1: complex, c2: complex) -> complex:
        """
        Divides two complex numbers.

        Args:
            c1: The first complex number.
            c2: The second complex number.

        Returns:
            The quotient of the two complex numbers.

        Examples:
            >>> ComplexCalculator.divide(1+2j, 3+4j)
            (0.44+0.08j)
        """
        return c1 / c2