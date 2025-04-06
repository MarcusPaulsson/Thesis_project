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
        result = ""
        i = 0
        while i < len(string):
            if string[i] == '&' and i + 1 < len(string) and string[i+1] == '#':
                j = i + 2
                is_hex = False
                if j < len(string) and string[j] == 'x':
                    is_hex = True
                    j += 1

                end = j
                while end < len(string) and string[end].isalnum():
                    end += 1

                if end < len(string) and string[end] == ';':
                    try:
                        if is_hex:
                            char_code = int(string[j:end], 16)
                        else:
                            char_code = int(string[j:end])

                        result += chr(char_code)
                        i = end + 1
                    except ValueError:
                        result += string[i]
                        i += 1
                else:
                    result += string[i]
                    i += 1
            else:
                result += string[i]
                i += 1
        return result


    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """
        return char.isdigit() or 'a' <= char <= 'f' or 'A' <= char <= 'F'