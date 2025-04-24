class NumberConverter:
    """
    The class allows converting decimal to binary, octal, and hexadecimal formats, and vice versa.
    """

    @staticmethod
    def decimal_to_binary(decimal_num: int) -> str:
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        """
        return bin(decimal_num)[2:]

    @staticmethod
    def binary_to_decimal(binary_num: str) -> int:
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        """
        return int(binary_num, 2)

    @staticmethod
    def decimal_to_octal(decimal_num: int) -> str:
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        """
        return oct(decimal_num)[2:]

    @staticmethod
    def octal_to_decimal(octal_num: str) -> int:
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal number
        :return: int, the decimal representation of octal number str.
        """
        return int(octal_num, 8)

    @staticmethod
    def decimal_to_hex(decimal_num: int) -> str:
        """
        Convert a number from decimal format to hexadecimal format.
        :param decimal_num: int, decimal number
        :return: str, the hexadecimal representation of an integer.
        """
        return hex(decimal_num)[2:]

    @staticmethod
    def hex_to_decimal(hex_num: str) -> int:
        """
        Convert a number from hexadecimal format to decimal format.
        :param hex_num: str, hexadecimal number
        :return: int, the decimal representation of hex number str.
        """
        return int(hex_num, 16)