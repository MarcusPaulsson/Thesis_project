class BinaryDataProcessor:
    """
    This is a class used to process binary data, which includes functions such as clearing non 0 or 1 characters, counting binary string information, and converting to corresponding strings based on different encoding methods.
    """

    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non 0 or 1 characters.
        """
        self.binary_string = ''.join(char for char in self.binary_string if char in '01')

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        bit_length = len(self.binary_string)
        if bit_length == 0:
            return {'Bit length': 0, 'Ones': 0, 'Zeroes': 0}

        zeroes = self.binary_string.count('0')
        ones = self.binary_string.count('1')
        zeroes_percentage = zeroes / bit_length
        ones_percentage = ones / bit_length

        return {'Zeroes': zeroes_percentage, 'Ones': ones_percentage, 'Bit length': bit_length}

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        ascii_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            if len(byte) == 8:
                try:
                    decimal_value = int(byte, 2)
                    ascii_string += chr(decimal_value)
                except ValueError:
                    # Handle cases where the byte is not a valid binary representation
                    pass
        return ascii_string

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        return self.convert_to_ascii()