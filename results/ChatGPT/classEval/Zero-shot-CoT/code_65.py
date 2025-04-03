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
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if isinstance(x, float):
            integer_part = str(int(x))
            decimal_part = str(x).split('.')[1]
        else:
            integer_part = str(x)
            decimal_part = ""
        
        words = self.parse_integer_part(integer_part)
        
        if decimal_part:
            words += " POINT " + " ".join(self.NUMBER[int(digit)] for digit in decimal_part)
        
        return words + " ONLY"

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        return self.format(float(x))

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif num < 20:
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
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        num = int(s)
        hundred = num // 100
        remainder = num % 100
        words = self.NUMBER[hundred] + " HUNDRED"
        if remainder > 0:
            words += " AND " + self.trans_two(str(remainder))
        return words.strip()

    def parse_integer_part(self, integer_part):
        """
        Converts the integer part of a number into words format
        :param integer_part: str, the integer part of the number
        :return: str, the integer part in words format
        """
        num = int(integer_part)
        if num == 0:
            return "ZERO"
        
        words = []
        index = 0

        while num > 0:
            if num % 1000 != 0:
                words.append(self.trans_three(str(num % 1000)) + (" " + self.NUMBER_MORE[index] if index > 0 else ""))
            num //= 1000
            index += 1

        return " ".join(reversed(words)).strip()

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        return self.NUMBER_MORE[i]