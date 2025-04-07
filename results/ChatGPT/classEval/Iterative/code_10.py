class BinaryDataProcessor:
    """
    This is a class used to process binary data, including functions such as clearing non-0 or 1 characters,
    counting binary string information, and converting to corresponding strings based on different encoding methods.
    """

    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non-0 or 1 characters.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non-0 or 1 characters.
        """
        self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
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
        Convert the binary string to ASCII string.
        """
        ascii_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i + 8]
            if len(byte) == 8:
                ascii_string += chr(int(byte, 2))
        return ascii_string

    def convert_to_utf8(self):
        """
        Convert the binary string to UTF-8 string.
        """
        return self.convert_to_ascii()  # In this context, ASCII is a subset of UTF-8