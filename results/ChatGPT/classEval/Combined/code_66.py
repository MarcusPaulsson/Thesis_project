import re


class NumericEntityUnescaper:
    """
    Class to replace numeric entities with their corresponding characters in a given string.
    """

    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string 
        with their corresponding Unicode characters.

        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced.
        """
        def replace_entity(match):
            entity = match.group(0)
            is_hex = entity.startswith("&#X") or entity.startswith("&#x")
            number_str = entity[3:-1]  # Extract number part
            
            # Validate and convert the number
            try:
                code_point = int(number_str, 16) if is_hex else int(number_str)
                return chr(code_point) if 0 <= code_point <= 0x10FFFF else entity
            except ValueError:
                return entity  # Return original if conversion fails

        regex = r'&#X?[0-9a-fA-F]+;'
        return re.sub(regex, replace_entity, string)

    @staticmethod
    def is_hex_char(char):
        """
        Determines if a character is a hexadecimal digit.

        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        """
        return char.lower() in '0123456789abcdef'

