class BinaryDataProcessor:
    """
    This class processes binary data, providing functionalities for cleaning,
    analyzing, and converting binary strings.
    """

    def __init__(self, binary_string):
        """
        Initializes the BinaryDataProcessor with a binary string and cleans it.

        Args:
            binary_string (str): The binary string to process.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Removes any characters that are not '0' or '1' from the binary string.
        """
        self.binary_string = ''.join(c for c in self.binary_string if c in '01')

    def calculate_binary_info(self):
        """
        Calculates and returns information about the binary string,
        including the percentage of zeroes and ones, and the total length.

        Returns:
            dict: A dictionary containing the 'Zeroes' percentage, 'Ones' percentage,
                  and 'Bit length'.  Returns all 0 if binary string is empty.
        """
        length = len(self.binary_string)
        if length == 0:
            return {'Zeroes': 0, 'Ones': 0, 'Bit length': 0}

        zeros = self.binary_string.count('0')
        ones = self.binary_string.count('1')

        zero_percentage = zeros / length
        one_percentage = ones / length

        return {'Zeroes': zero_percentage, 'Ones': one_percentage, 'Bit length': length}

    def convert_to_ascii(self):
        """
        Converts the binary string to an ASCII string. Each 8-bit sequence
        is treated as an ASCII character code.

        Returns:
            str: The ASCII string representation of the binary data.
                 Returns an empty string if the binary string length is not a multiple of 8.
        """
        if len(self.binary_string) % 8 != 0:
            return ""

        ascii_string = ""
        for i in range(0, len(self.binary_string), 8):
            octet = self.binary_string[i:i + 8]
            decimal_value = int(octet, 2)
            ascii_string += chr(decimal_value)
        return ascii_string

    def convert_to_utf8(self):
        """
        Converts the binary string to a UTF-8 string. Each 8-bit sequence
        is treated as a UTF-8 character code.

        Returns:
            str: The UTF-8 string representation of the binary data.
                 Returns an empty string if the binary string length is not a multiple of 8.
        """
        if len(self.binary_string) % 8 != 0:
            return ""

        utf8_string = ""
        for i in range(0, len(self.binary_string), 8):
            octet = self.binary_string[i:i + 8]
            decimal_value = int(octet, 2)
            utf8_string += chr(decimal_value)
        return utf8_string