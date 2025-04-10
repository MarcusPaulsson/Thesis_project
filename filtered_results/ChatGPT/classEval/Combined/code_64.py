class NumberConverter:
    """
    A class for converting numbers between decimal, binary, octal, and hexadecimal formats.
    """

    @staticmethod
    def decimal_to_binary(decimal_num: int) -> str:
        """
        Convert a decimal number to its binary representation.
        
        :param decimal_num: int, the decimal number to convert
        :return: str, the binary representation of the number
        """
        return bin(decimal_num)[2:]

    @staticmethod
    def binary_to_decimal(binary_num: str) -> int:
        """
        Convert a binary number to its decimal representation.
        
        :param binary_num: str, the binary number to convert
        :return: int, the decimal representation of the binary number
        """
        return int(binary_num, 2)

    @staticmethod
    def decimal_to_octal(decimal_num: int) -> str:
        """
        Convert a decimal number to its octal representation.
        
        :param decimal_num: int, the decimal number to convert
        :return: str, the octal representation of the number
        """
        return oct(decimal_num)[2:]

    @staticmethod
    def octal_to_decimal(octal_num: str) -> int:
        """
        Convert an octal number to its decimal representation.
        
        :param octal_num: str, the octal number to convert
        :return: int, the decimal representation of the octal number
        """
        return int(octal_num, 8)

    @staticmethod
    def decimal_to_hex(decimal_num: int) -> str:
        """
        Convert a decimal number to its hexadecimal representation.
        
        :param decimal_num: int, the decimal number to convert
        :return: str, the hexadecimal representation of the number
        """
        return hex(decimal_num)[2:]

    @staticmethod
    def hex_to_decimal(hex_num: str) -> int:
        """
        Convert a hexadecimal number to its decimal representation.
        
        :param hex_num: str, the hexadecimal number to convert
        :return: int, the decimal representation of the hexadecimal number
        """
        return int(hex_num, 16)