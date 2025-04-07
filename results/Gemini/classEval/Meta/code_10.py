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
        >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        >>> bdp.clean_non_binary_chars()
        >>> bdp.binary_string
        '0110100001100101011011000110110001101111'

        """
        cleaned_string = ''.join(char for char in self.binary_string if char in '01')
        self.binary_string = cleaned_string

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
        bit_length = len(self.binary_string)
        if bit_length == 0:
            return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
        zeroes = self.binary_string.count('0') / bit_length
        ones = self.binary_string.count('1') / bit_length
        return {'Zeroes': zeroes, 'Ones': ones, 'Bit length': bit_length}

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'

        """
        ascii_string = ''
        for i in range(0, len(self.binary_string), 8):
            binary_octet = self.binary_string[i:i + 8]
            if len(binary_octet) == 8:
                ascii_string += chr(int(binary_octet, 2))
        return ascii_string

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_utf8()
        'hello'

        """
        utf8_string = ''
        for i in range(0, len(self.binary_string), 8):
            binary_octet = self.binary_string[i:i + 8]
            if len(binary_octet) == 8:
                utf8_string += chr(int(binary_octet, 2))
        return utf8_string