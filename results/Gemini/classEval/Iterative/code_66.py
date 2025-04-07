import re

class NumericEntityUnescaper:
    """
    Replaces numeric character references (HTML entities) in a string with their corresponding Unicode characters.
    """

    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.

        Args:
            string: The input string containing numeric character references.

        Returns:
            The input string with numeric character references replaced with their corresponding Unicode characters.
        """

        def replace_entity(match):
            entity = match.group(1)
            try:
                if entity.startswith('x'):
                    cp = int(entity[1:], 16)
                else:
                    cp = int(entity, 10)

                # Check for valid Unicode code points
                if 0 <= cp <= 0x10FFFF:
                    return chr(cp)
                else:
                    return match.group(0)  # Return original entity if invalid

            except ValueError:
                return match.group(0)  # Return original entity if conversion fails

        return re.sub(r"&#(x?[0-9a-fA-F]+);", replace_entity, string)


    @staticmethod
    def is_hex_char(char):
        """
        Checks if a character is a hexadecimal digit.

        Args:
            char: The character to check.

        Returns:
            True if the character is a hexadecimal digit, False otherwise.
        """
        return '0' <= char <= '9' or 'a' <= char <= 'f' or 'A' <= char <= 'F'