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
            return '0'

        binary_num = ''
        while decimal_num > 0:
            remainder = decimal_num % 2
            binary_num = str(remainder) + binary_num
            decimal_num //= 2
        return binary_num

    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        """
        if not isinstance(binary_num, str):
            raise TypeError("Input must be a string.")

        if not all(digit in '01' for digit in binary_num):
            raise ValueError("Input must be a valid binary string (containing only '0' and '1').")

        decimal_num = 0
        power = 0
        for digit in reversed(binary_num):
            if digit == '1':
                decimal_num += 2 ** power
            power += 1
        return decimal_num

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
            return '0'

        octal_num = ''
        while decimal_num > 0:
            remainder = decimal_num % 8
            octal_num = str(remainder) + octal_num
            decimal_num //= 8
        return octal_num

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

        decimal_num = 0
        power = 0
        for digit in reversed(octal_num):
            decimal_num += int(digit) * (8 ** power)
            power += 1
        return decimal_num

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

        hex_digits = "0123456789abcdef"
        if decimal_num == 0:
            return '0'

        hex_num = ''
        while decimal_num > 0:
            remainder = decimal_num % 16
            hex_num = hex_digits[remainder] + hex_num
            decimal_num //= 16
        return hex_num

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
        if not all(digit in '0123456789abcdef' for digit in hex_num):
            raise ValueError("Input must be a valid hexadecimal string.")

        decimal_num = 0
        power = 0
        for digit in reversed(hex_num):
            if '0' <= digit <= '9':
                value = int(digit)
            else:
                value = ord(digit) - ord('a') + 10
            decimal_num += value * (16 ** power)
            power += 1
        return decimal_num