class NumberConverter:
    """
    The class allows to convert decimal to binary, octal, and hexadecimal respectively, and vice versa.
    """

    @staticmethod
    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        :raises TypeError: if input is not an integer.
        :raises ValueError: if input is a negative integer.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """
        if not isinstance(decimal_num, int):
            raise TypeError("Input must be an integer.")
        if decimal_num < 0:
            raise ValueError("Input must be a non-negative integer.")

        return bin(decimal_num)[2:]

    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        :raises TypeError: if input is not a string.
        :raises ValueError: if input is not a valid binary string.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
        if not isinstance(binary_num, str):
            raise TypeError("Input must be a string.")
        if not all(bit in '01' for bit in binary_num):
            raise ValueError("Input must be a valid binary string.")

        return int(binary_num, 2)

    @staticmethod
    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        :raises TypeError: if input is not an integer.
        :raises ValueError: if input is a negative integer.
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
        if not isinstance(decimal_num, int):
            raise TypeError("Input must be an integer.")
        if decimal_num < 0:
            raise ValueError("Input must be a non-negative integer.")

        return oct(decimal_num)[2:]

    @staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        :raises TypeError: if input is not a string.
        :raises ValueError: if input is not a valid octal string.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
        if not isinstance(octal_num, str):
            raise TypeError("Input must be a string.")
        if not all(digit in '01234567' for digit in octal_num):
            raise ValueError("Input must be a valid octal string.")

        return int(octal_num, 8)

    @staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        :raises TypeError: if input is not an integer.
        :raises ValueError: if input is a negative integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """
        if not isinstance(decimal_num, int):
            raise TypeError("Input must be an integer.")
        if decimal_num < 0:
            raise ValueError("Input must be a non-negative integer.")

        return hex(decimal_num)[2:]

    @staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        :raises TypeError: if input is not a string.
        :raises ValueError: if input is not a valid hexadecimal string.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
        if not isinstance(hex_num, str):
            raise TypeError("Input must be a string.")
        if not all(digit in '0123456789abcdefABCDEF' for digit in hex_num):
            raise ValueError("Input must be a valid hexadecimal string.")

        return int(hex_num, 16)