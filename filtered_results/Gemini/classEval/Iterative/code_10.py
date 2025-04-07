class BinaryDataProcessor:
    """
    This class processes binary data, offering functionalities like cleaning non-binary characters,
    calculating binary string information, and converting to strings using different encodings.
    """

    def __init__(self, binary_string):
        """
        Initializes the class with a binary string and cleans it, removing non 0 or 1 characters.

        Args:
            binary_string (str): The binary string to process.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Cleans the binary string by removing any characters that are not 0 or 1.
        """
        self.binary_string = ''.join(char for char in self.binary_string if char in '01')

    def calculate_binary_info(self):
        """
        Calculates and returns information about the binary string,
        including the percentage of 0s and 1s, and the total length.

        Returns:
            dict: A dictionary containing the percentages of '0' and '1', and the bit length.
                  Returns {'Zeroes': 0, 'Ones': 0, 'Bit length': 0} if the string is empty.
        """
        total_length = len(self.binary_string)
        if total_length == 0:
            return {'Zeroes': 0, 'Ones': 0, 'Bit length': 0}

        zeroes = self.binary_string.count('0')
        ones = self.binary_string.count('1')

        zeroes_percentage = zeroes / total_length
        ones_percentage = ones / total_length

        return {'Zeroes': zeroes_percentage, 'Ones': ones_percentage, 'Bit length': total_length}

    def convert_to_ascii(self):
        """
        Converts the binary string to an ASCII string. Each 8-bit chunk is converted to its
        corresponding ASCII character.  If the binary string length is not a multiple of 8,
        the remaining bits are ignored.

        Returns:
            str: The resulting ASCII string. Returns an empty string if the binary string is empty
                 or if no complete 8-bit chunks are available.
        """
        return self._convert_to_string(encoding='ascii')

    def convert_to_utf8(self):
        """
        Converts the binary string to a UTF-8 string. Each 8-bit chunk is converted to its
        corresponding UTF-8 character. If the binary string length is not a multiple of 8,
        the remaining bits are ignored.

        Returns:
            str: The resulting UTF-8 string. Returns an empty string if the binary string is empty
                 or if no complete 8-bit chunks are available.
        """
        return self._convert_to_string(encoding='utf-8')

    def _convert_to_string(self, encoding='utf-8'):
        """
        Helper function to convert the binary string to a string using the specified encoding.

        Args:
            encoding (str): The encoding to use ('ascii' or 'utf-8').  Defaults to 'utf-8'.

        Returns:
            str: The resulting string.
        """
        result_string = ""
        for i in range(0, len(self.binary_string), 8):
            binary_chunk = self.binary_string[i:i + 8]
            if len(binary_chunk) == 8:
                try:
                    decimal_value = int(binary_chunk, 2)
                    result_string += chr(decimal_value)
                except ValueError:
                    # Handle cases where the decimal value is outside the valid range for chr()
                    return "" # Or raise an exception, depending on desired behavior
        return result_string