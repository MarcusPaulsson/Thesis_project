import re


class NumericEntityUnescaper:
    """
    This is a class that provides functionality to replace numeric entities with their corresponding characters in a given string.
    """

    def __init__(self):
        pass

    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'
        """
        def replace_entity(match):
            entity = match.group(0)
            if entity.startswith("&#x") or entity.startswith("&#X"):
                try:
                    char_code = int(entity[3:-1], 16)
                    return chr(char_code)
                except ValueError:
                    return entity
            elif entity.startswith("&#"):
                try:
                    char_code = int(entity[2:-1])
                    return chr(char_code)
                except ValueError:
                    return entity
            return entity

        return re.sub(r'&#[xX]?[0-9a-fA-F]*;|&#\d+;', replace_entity, string)

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True
        """
        return char.lower() in '0123456789abcdef'
