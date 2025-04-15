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
            if string[i:i+2] == "&#":
                j = i + 2
                while j < len(string) and string[j].isdigit():
                    j += 1
                if j > i + 2:
                    try:
                        code = int(string[i+2:j])
                        result += chr(code)
                        i = j
                    except ValueError:
                        result += string[i]
                        i += 1
                else:
                    result += string[i]
                    i += 1
            elif string[i:i+3] == "&#x":
                j = i + 3
                while j < len(string) and self.is_hex_char(string[j]):
                    j += 1
                if j > i + 3:
                    try:
                        code = int(string[i+3:j], 16)
                        result += chr(code)
                        i = j
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
        return '0' <= char <= '9' or 'a' <= char <= 'f' or 'A' <= char <= 'F'