import re

class NumericEntityUnescaper:
    """
    This class provides functionality to replace numeric entities with their corresponding characters in a given string.
    """

    def replace(self, string: str) -> str:
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        """
        def replace_entity(match):
            entity = match.group(0)
            try:
                if entity.startswith("&#X") or entity.startswith("&#x"):
                    code_point = int(entity[3:-1], 16)
                else:
                    code_point = int(entity[2:-1])
                return chr(code_point)
            except (ValueError, IndexError):
                return entity  # Return the original entity if it cannot be converted

        return re.sub(r'&#[Xx]?[0-9a-fA-F]+;|&#\d+;', replace_entity, string)

    @staticmethod
    def is_hex_char(char: str) -> bool:
        """
        Determines whether a given character is a hexadecimal digit.
        
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        """
        return char.lower() in '0123456789abcdef'