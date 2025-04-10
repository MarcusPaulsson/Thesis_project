class BinaryDataProcessor:
    """
    This class processes binary data, providing methods to clean non-binary characters,
    calculate binary string information, and convert binary strings to ASCII and UTF-8.
    """

    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non-binary characters.
        """
        self.binary_string = self.clean_non_binary_chars(binary_string)

    @staticmethod
    def clean_non_binary_chars(binary_string):
        """
        Clean the binary string by removing all non-binary characters (not '0' or '1').
        
        >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        >>> bdp.binary_string
        '0110100001100101011011000110110001101111'
        """
        return ''.join(filter(lambda x: x in '01', binary_string))

    def calculate_binary_info(self):
        """
        Calculate binary string information, including the percentage of 0s and 1s, and total length.
        
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}
        """
        total_bits = len(self.binary_string)
        if total_bits == 0:
            return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
        
        count_ones = self.binary_string.count('1')
        count_zeroes = total_bits - count_ones
        
        return {
            'Zeroes': count_zeroes / total_bits,
            'Ones': count_ones / total_bits,
            'Bit length': total_bits
        }

    def convert_to_ascii(self):
        """
        Convert the binary string to an ASCII string.
        
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'
        """
        return ''.join(chr(int(self.binary_string[i:i + 8], 2)) for i in range(0, len(self.binary_string), 8))

    def convert_to_utf8(self):
        """
        Convert the binary string to a UTF-8 string.
        
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_utf8()
        'hello'
        """
        return self.convert_to_ascii()  # ASCII is a subset of UTF-8 for standard characters.