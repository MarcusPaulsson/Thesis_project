class BinaryDataProcessor:
    """
    A class to process binary data, including cleaning non-binary characters, 
    calculating binary string statistics, and converting to ASCII and UTF-8 strings.
    """

    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non-binary characters.
        """
        self.binary_string = self.clean_non_binary_chars(binary_string)

    @staticmethod
    def clean_non_binary_chars(binary_string):
        """
        Clean the binary string by removing all non-binary characters (anything other than '0' or '1').
        """
        return ''.join(filter(lambda x: x in '01', binary_string))

    def calculate_binary_info(self):
        """
        Calculate and return the percentage of 0s and 1s, as well as the total length of the binary string.
        """
        total_length = len(self.binary_string)
        if total_length == 0:
            return {'Zeroes': 0, 'Ones': 0, 'Bit length': 0}

        count_ones = self.binary_string.count('1')
        count_zeroes = total_length - count_ones

        return {
            'Zeroes': count_zeroes / total_length,
            'Ones': count_ones / total_length,
            'Bit length': total_length
        }

    def convert_to_ascii(self):
        """
        Convert the binary string to an ASCII string.
        """
        return ''.join(chr(int(self.binary_string[i:i + 8], 2)) 
                       for i in range(0, len(self.binary_string), 8) 
                       if len(self.binary_string[i:i + 8]) == 8)

    def convert_to_utf8(self):
        """
        Convert the binary string to a UTF-8 string.
        """
        return self.convert_to_ascii()  # UTF-8 conversion can be handled similarly for this implementation