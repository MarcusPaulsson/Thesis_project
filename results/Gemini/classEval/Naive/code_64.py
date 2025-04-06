class NumberConverter:
    """
    The class allows to convert  decimal to binary, octal and hexadecimal repectively and contrarily
    """

    @staticmethod
    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        """
        if not isinstance(decimal_num, int):
            raise TypeError("Input must be an integer.")

        if decimal_num < 0:
            raise ValueError("Input must be a non-negative integer.")

        if decimal_num == 0:
            return "0"

        binary_representation = ""
        while decimal_num > 0:
            remainder = decimal_num % 2
            binary_representation = str(remainder) + binary_representation
            decimal_num //= 2

        return binary_representation

    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        """
        if not isinstance(binary_num, str):
            raise TypeError("Input must be a string.")

        if not all(bit in '01' for bit in binary_num):
            raise ValueError("Input must be a valid binary string (containing only '0' and '1').")

        decimal_representation = 0
        power = 0
        for bit in reversed(binary_num):
            if bit == '1':
                decimal_representation += 2 ** power
            power += 1

        return decimal_representation

    @staticmethod
    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        """
        if not isinstance(decimal_num, int):
            raise TypeError("Input must be an integer.")
        
        if decimal_num < 0:
            raise ValueError("Input must be a non-negative integer.")

        if decimal_num == 0:
            return "0"

        octal_representation = ""
        while decimal_num > 0:
            remainder = decimal_num % 8
            octal_representation = str(remainder) + octal_representation
            decimal_num //= 8

        return octal_representation

    @staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        """
        if not isinstance(octal_num, str):
            raise TypeError("Input must be a string.")
        
        if not all(digit in '01234567' for digit in octal_num):
            raise ValueError("Input must be a valid octal string (containing only digits 0-7).")

        decimal_representation = 0
        power = 0
        for digit in reversed(octal_num):
            decimal_representation += int(digit) * (8 ** power)
            power += 1

        return decimal_representation

    @staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        """
        if not isinstance(decimal_num, int):
            raise TypeError("Input must be an integer.")

        if decimal_num < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        if decimal_num == 0:
            return "0"

        hex_representation = ""
        hex_chars = "0123456789abcdef"

        while decimal_num > 0:
            remainder = decimal_num % 16
            hex_representation = hex_chars[remainder] + hex_representation
            decimal_num //= 16

        return hex_representation

    @staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        """
        if not isinstance(hex_num, str):
            raise TypeError("Input must be a string.")

        hex_num = hex_num.lower()
        if not all(char in '0123456789abcdef' for char in hex_num):
            raise ValueError("Input must be a valid hexadecimal string (containing only digits 0-9 and letters a-f).")

        decimal_representation = 0
        power = 0
        for char in reversed(hex_num):
            if '0' <= char <= '9':
                digit = ord(char) - ord('0')
            else:
                digit = ord(char) - ord('a') + 10

            decimal_representation += digit * (16 ** power)
            power += 1

        return decimal_representation