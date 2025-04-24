class BigNumCalculator:
    """
    A class that implements big number calculations, including addition, subtraction, and multiplication.
    """

    @staticmethod
    def add(num1: str, num2: str) -> str:
        """
        Adds two big numbers represented as strings.
        
        :param num1: The first number to add, str.
        :param num2: The second number to add, str.
        :return: The sum of the two numbers, str.
        """
        return str(int(num1) + int(num2))

    @staticmethod
    def subtract(num1: str, num2: str) -> str:
        """
        Subtracts two big numbers represented as strings.
        
        :param num1: The first number to subtract, str.
        :param num2: The second number to subtract, str.
        :return: The difference of the two numbers, str.
        """
        return str(int(num1) - int(num2))

    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        """
        Multiplies two big numbers represented as strings.
        
        :param num1: The first number to multiply, str.
        :param num2: The second number to multiply, str.
        :return: The product of the two numbers, str.
        """
        return str(int(num1) * int(num2))