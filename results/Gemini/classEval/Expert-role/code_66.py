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
            if string[i:i + 2] == "&#":
                j = i + 2
                is_hex = False
                if j < len(string) and string[j:j+1].lower() == 'x':
                    is_hex = True
                    j += 1
                
                end = string.find(";", j)
                if end != -1:
                    try:
                        if is_hex:
                            entity = string[j:end]
                            val = int(entity, 16)
                        else:
                            entity = string[j:end]
                            val = int(entity)
                        result += chr(val)
                        i = end + 1
                    except ValueError:
                        result += string[i:end+1]
                        i = end + 1
                    except OverflowError:
                        i += 2
                else:
                    result += string[i:i+2]
                    i += 2
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
        return '0' <= char <= '9' or 'a' <= char.lower() <= 'f'