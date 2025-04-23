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
        if decimal_num == 0:
            return "0"
        binary = ""
        while decimal_num > 0:
            remainder = decimal_num % 2
            binary = str(remainder) + binary
            decimal_num //= 2
        return binary

    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        """
        decimal = 0
        power = 0
        for digit in reversed(binary_num):
            if digit == '1':
                decimal += 2 ** power
            power += 1
        return decimal

    @staticmethod
    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        """
        if decimal_num == 0:
            return "0"
        octal = ""
        while decimal_num > 0:
            remainder = decimal_num % 8
            octal = str(remainder) + octal
            decimal_num //= 8
        return octal

    @staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        """
        decimal = 0
        power = 0
        for digit in reversed(octal_num):
            decimal += int(digit) * (8 ** power)
            power += 1
        return decimal

    @staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return: str, the hex representation of an integer.
        """
        if decimal_num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        hex_num = ""
        while decimal_num > 0:
            remainder = decimal_num % 16
            hex_num = hex_chars[remainder] + hex_num
            decimal_num //= 16
        return hex_num

    @staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        """
        decimal = 0
        power = 0
        hex_chars = "0123456789abcdef"
        for digit in reversed(hex_num):
            decimal += hex_chars.index(digit) * (16 ** power)
            power += 1
        return decimal