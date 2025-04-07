import re
import unittest

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
            try:
                if entity.startswith('&#X') or entity.startswith('&#x'):
                    code_point = int(entity[3:-1], 16)
                else:
                    code_point = int(entity[2:-1])
                return chr(code_point)
            except ValueError:
                return entity  # Return the original entity if it cannot be converted

        return re.sub(r'&#X?[0-9A-Fa-f]+;', replace_entity, string)

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True
        """
        return char in '0123456789abcdefABCDEF'


class NumericEntityUnescaperTestReplace(unittest.TestCase):
    def test_replace_1(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#65;&#66;&#67;")
        self.assertEqual(res, "ABC")

    def test_replace_2(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#65;&#65;&#65;")
        self.assertEqual(res, "AAA")

    def test_replace_3(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#66;&#66;&#66;")
        self.assertEqual(res, "BBB")

    def test_replace_4(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#67;&#67;&#67;")
        self.assertEqual(res, "CCC")

    def test_replace_5(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("")
        self.assertEqual(res, "")

    def test_replace_6(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#")
        self.assertEqual(res, "")

    def test_replace_7(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#X65;&#66;&#67;")
        self.assertEqual(res, "eBC")

    def test_replace_8(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#???;&#66;&#67;")
        self.assertEqual(res, "&#???;BC")

    def test_replace_9(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#67;&#67;&#67;;")
        self.assertEqual(res, "CCC")

    def test_replace_10(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#X")
        self.assertEqual(res, "")

    def test_replace_11(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#c1d;&#66;&#67;")
        self.assertEqual(res, "")


class NumericEntityUnescaperTestIsHexChar(unittest.TestCase):
    def test_is_hex_char_1(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('0')
        self.assertEqual(res, True)

    def test_is_hex_char_2(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('F')
        self.assertEqual(res, True)

    def test_is_hex_char_3(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('G')
        self.assertEqual(res, False)

    def test_is_hex_char_4(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('X')
        self.assertEqual(res, False)

    def test_is_hex_char_5(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('Z')
        self.assertEqual(res, False)


class unescaperTest(unittest.TestCase):
    def test_numericentityunescaper(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#65;&#66;&#67;")
        self.assertEqual(res, "ABC")

        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('0')
        self.assertEqual(res, True)

# Uncomment the following line to run the tests
# unittest.main()