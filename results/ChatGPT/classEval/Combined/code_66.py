import re


class NumericEntityUnescaper:
    """
    A class that provides functionality to replace numeric entities with their corresponding characters in a given string.
    """

    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.

        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        """
        def replace_entity(match):
            entity = match.group(0)
            # Check for decimal or hexadecimal entity
            if entity.startswith("&#x") or entity.startswith("&#X"):
                hex_value = entity[3:-1]
                if self.is_valid_hex(hex_value):
                    return chr(int(hex_value, 16))
            elif entity.startswith("&#"):
                decimal_value = entity[2:-1]
                if decimal_value.isdigit():
                    return chr(int(decimal_value))
            return entity  # Return the original entity if no valid match

        # Regular expression to find numeric entities
        pattern = r'&#[xX]?[0-9a-fA-F]+;|&#\d+;'
        return re.sub(pattern, replace_entity, string)

    @staticmethod
    def is_valid_hex(hex_value):
        """
        Validates if the hex_value is a valid hexadecimal number.

        :param hex_value: str, the string to check for hexadecimal validity.
        :return: bool, True if valid, False otherwise.
        """
        return bool(hex_value) and all(c in '0123456789abcdefABCDEF' for c in hex_value)

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.

        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        """
        return char in '0123456789abcdefABCDEF'

