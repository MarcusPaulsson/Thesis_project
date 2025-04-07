class NumberWordFormatter:
    """
    This is a class that provides to convert numbers into their corresponding English word representation, including handling the conversion of both the integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, x):
        """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        """
        if x is None:
            return ""
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = int(round((x - integer_part) * 100))
        else:
            integer_part = int(x)
            decimal_part = 0
        
        words = self.convert_integer_to_words(integer_part)
        if decimal_part > 0:
            words += " AND CENTS " + self.trans_two(str(decimal_part))
        words += " ONLY"
        return words

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        return self.format(float(x))

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif 10 <= num < 20:
            return self.NUMBER_TEEN[num - 10]
        else:
            ten = num // 10
            one = num % 10
            return self.NUMBER_TEN[ten - 1] + (" " + self.NUMBER[one] if one > 0 else "")

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        num = int(s)
        if num < 100:
            return self.trans_two(s)
        
        hundred = num // 100
        remainder = num % 100
        result = self.NUMBER[hundred] + " HUNDRED"
        if remainder > 0:
            result += " AND " + self.trans_two(str(remainder))
        return result

    def convert_integer_to_words(self, num):
        """
        Converts an integer into words format
        :param num: int, the integer to be converted
        :return: str, the number in words format
        """
        if num == 0:
            return "ZERO"
        
        words = ""
        index = 0
        
        while num > 0:
            if num % 1000 != 0:
                words = self.trans_three(str(num % 1000)) + (" " + self.NUMBER_MORE[index] if index > 0 else "") + (" " + words if words else "")
            num //= 1000
            index += 1
        
        return words.strip()

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        return self.NUMBER_MORE[i]