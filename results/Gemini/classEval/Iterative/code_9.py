class BigNumCalculator:
    """
    This is a class that implements big number calculations, including adding, subtracting and multiplying.
    """

    @staticmethod
    def add(num1, num2):
        """
        Adds two big numbers represented as strings.

        Handles arbitrarily large positive or negative integers.

        :param num1: The first number to add, represented as a string.
        :param num2: The second number to add, represented as a string.
        :return: The sum of the two numbers, represented as a string.
        :raises ValueError: If either input is not a valid integer string.

        >>> BigNumCalculator.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'
        >>> BigNumCalculator.add("-123", "456")
        '333'
        >>> BigNumCalculator.add("123", "-456")
        '-333'
        """
        try:
            n1 = num1.strip()
            n2 = num2.strip()
            
            if not (BigNumCalculator._is_valid_integer_string(n1) and BigNumCalculator._is_valid_integer_string(n2)):
                raise ValueError("Invalid input: Both inputs must be valid integer strings.")

            result = str(int(n1) + int(n2))
            return result
        except ValueError as e:
            raise ValueError(str(e))

    @staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers represented as strings.

        Handles arbitrarily large positive or negative integers.

        :param num1: The first number to subtract, represented as a string.
        :param num2: The second number to subtract, represented as a string.
        :return: The difference of the two numbers, represented as a string.
        :raises ValueError: If either input is not a valid integer string.

        >>> BigNumCalculator.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'
        >>> BigNumCalculator.subtract("456", "123")
        '333'
        >>> BigNumCalculator.subtract("123", "456")
        '-333'
        """
        try:
            n1 = num1.strip()
            n2 = num2.strip()
            
            if not (BigNumCalculator._is_valid_integer_string(n1) and BigNumCalculator._is_valid_integer_string(n2)):
                raise ValueError("Invalid input: Both inputs must be valid integer strings.")

            result = str(int(n1) - int(n2))
            return result
        except ValueError as e:
            raise ValueError(str(e))

    @staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers represented as strings.

        Handles arbitrarily large positive or negative integers.

        :param num1: The first number to multiply, represented as a string.
        :param num2: The second number to multiply, represented as a string.
        :return: The product of the two numbers, represented as a string.
        :raises ValueError: If either input is not a valid integer string.

        >>> BigNumCalculator.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'
        >>> BigNumCalculator.multiply("12", "34")
        '408'
        >>> BigNumCalculator.multiply("-12", "34")
        '-408'
        """
        try:
            n1 = num1.strip()
            n2 = num2.strip()

            if not (BigNumCalculator._is_valid_integer_string(n1) and BigNumCalculator._is_valid_integer_string(n2)):
                raise ValueError("Invalid input: Both inputs must be valid integer strings.")
            
            result = str(int(n1) * int(n2))
            return result
        except ValueError as e:
            raise ValueError(str(e))
    
    @staticmethod
    def _is_valid_integer_string(s):
        """
        Checks if a string represents a valid integer.
        :param s: The string to check.
        :return: True if the string is a valid integer, False otherwise.
        """
        if not isinstance(s, str):
            return False
        if not s:
            return False
        if s[0] == '-' and len(s) > 1:
            s = s[1:]  # Remove the negative sign for the rest of the check
        return s.isdigit()