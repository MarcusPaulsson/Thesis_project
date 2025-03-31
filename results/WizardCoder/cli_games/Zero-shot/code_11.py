class BinaryDataProcessor:
    """
    This is a class used to process binary data, which includes functions such as clearing non 0 or 1 characters,
    counting binary string information, and converting to corresponding strings based on different encoding methods.
    """

    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        """
        self.binary_string = ''.join([char for char in binary_string if char == '0' or char == '1'])

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("01101000daf3e4r011010101101100011011000110111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 24}
        """
        binary_length = len(self.binary_string)
        zero_count = self.binary_string.count('0')
        one_count = self.binary_string.count('1')
        info_dict = {
            'Zeroes': zero_count / binary_length,
            'Ones': one_count / binary_length,
            'Bit length': binary_length
        }
        return info_dict

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        >>> bdp = BinaryDataProcessor("011010000110010101101100011011000110111")
        >>> bdp.convert_to_ascii()
        'hello'
        """
        bitstring = self.binary_string[:8]
        ascii_chars = []
        while len(bitstring) >= 8:
            char_value = int(bitstring[:8], 2)
            ascii_char = chr(char_value)
            if ord(ascii_char) == 0: # stop at the first null character
                break
            ascii_chars.append(ascii_char)
            bitstring = bitstring[8:]
        return ''.join(ascii_chars)

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        >>> bdp = BinaryDataProcessor("01101000110010101101100011011000110111")
        >>> bdp.convert_to_utf8()
        'hello'
        """
        bitstring = self.binary_string[:8]
        utf8_chars = []
        while len(bitstring) >= 24:
            char_value = int(bitstring[:24], 2)
            if char_value == 0: # stop at the first null character (24 bits with '1's and '0's equals a utf-8 character of value 0)
                break
            utf8_char = self.binary_string[:8].decode('utf-8')
            utf8_chars.append(utf8_char)
            bitstring = bitstring[24:]
        return ''.join(utf8_chars)