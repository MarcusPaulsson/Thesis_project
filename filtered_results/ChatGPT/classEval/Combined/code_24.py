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
