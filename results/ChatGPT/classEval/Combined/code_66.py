import re
import unittest

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


class NumericEntityUnescaperTestReplace(unittest.TestCase):
    def setUp(self):
        self.unescaper = NumericEntityUnescaper()

    def test_replace_valid(self):
        self.assertEqual(self.unescaper.replace("&#65;&#66;&#67;"), "ABC")
        self.assertEqual(self.unescaper.replace("&#X65;&#66;&#67;"), "eBC")
    
    def test_replace_repeated(self):
        self.assertEqual(self.unescaper.replace("&#65;&#65;&#65;"), "AAA")
        self.assertEqual(self.unescaper.replace("&#66;&#66;&#66;"), "BBB")
        self.assertEqual(self.unescaper.replace("&#67;&#67;&#67;"), "CCC")

    def test_replace_empty(self):
        self.assertEqual(self.unescaper.replace(""), "")
        self.assertEqual(self.unescaper.replace("&#"), "")
        self.assertEqual(self.unescaper.replace("&#X"), "")
        
    def test_replace_invalid(self):
        self.assertEqual(self.unescaper.replace("&#???;&#66;&#67;"), "&#???;BC")
        self.assertEqual(self.unescaper.replace("&#c1d;&#66;&#67;"), "")
        self.assertEqual(self.unescaper.replace("&#67;&#67;&#67;;"), "CCC")


class NumericEntityUnescaperTestIsHexChar(unittest.TestCase):
    def test_is_hex_char(self):
        unescaper = NumericEntityUnescaper()
        self.assertTrue(unescaper.is_hex_char('0'))
        self.assertTrue(unescaper.is_hex_char('F'))
        self.assertFalse(unescaper.is_hex_char('G'))
        self.assertFalse(unescaper.is_hex_char('X'))
        self.assertFalse(unescaper.is_hex_char('Z'))


if __name__ == '__main__':
    unittest.main()