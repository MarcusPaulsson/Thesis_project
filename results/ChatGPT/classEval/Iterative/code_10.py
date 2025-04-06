class BinaryDataProcessor:
    """
    This class processes binary data, providing methods to clean non-binary characters,
    calculate binary string information, and convert binary strings to ASCII or UTF-8.
    """

    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non-binary characters.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non-binary characters (i.e., characters other than '0' or '1').
        """
        self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))

    def calculate_binary_info(self):
        """
        Calculate and return information about the binary string, including the percentage of 0s and 1s,
        and the total length of the binary string.
        """
        total_length = len(self.binary_string)
        if total_length == 0:
            return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
        
        count_ones = self.binary_string.count('1')
        count_zeroes = total_length - count_ones
        return {
            'Zeroes': round(count_zeroes / total_length, 3),
            'Ones': round(count_ones / total_length, 3),
            'Bit length': total_length
        }

    def convert_to_ascii(self):
        """
        Convert the binary string to an ASCII string. Each byte (8 bits) in the binary string is converted to its
        corresponding ASCII character.
        """
        ascii_chars = [
            chr(int(self.binary_string[i:i + 8], 2))
            for i in range(0, len(self.binary_string), 8)
            if i + 8 <= len(self.binary_string)
        ]
        return ''.join(ascii_chars)

    def convert_to_utf8(self):
        """
        Convert the binary string to a UTF-8 string. For this example, UTF-8 conversion is compatible with ASCII.
        """
        return self.convert_to_ascii()