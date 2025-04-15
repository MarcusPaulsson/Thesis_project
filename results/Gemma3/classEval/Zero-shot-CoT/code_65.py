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
                            "EIGHTEEN",
                            "NINETEEN"]
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
        if x is None:
            return ""
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = int(round((x - integer_part) * 100))
            integer_string = self.format(integer_part)
            decimal_string = self.trans_two(str(decimal_part).zfill(2))
            if integer_string and decimal_string:
                return integer_string + " AND CENTS " + decimal_string + " ONLY"
            elif integer_string:
                return integer_string + " ONLY"
            elif decimal_string:
                return "CENTS " + decimal_string + " ONLY"
            else:
                return "ZERO ONLY"
        elif isinstance(x, int):
            if x == 0:
                return "ZERO ONLY"
            else:
                result = ""
                i = 0
                while x > 0:
                    remainder = x % 1000
                    if remainder != 0:
                        result = self.trans_three(str(remainder).zfill(3)) + " " + self.NUMBER_MORE[i] + " " + result
                    x //= 1000
                    i += 1
                return result.strip() + " ONLY"
        else:
            return ""

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        try:
            return self.format(float(x))
        except ValueError:
            return ""

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        if len(s) == 2:
            first_digit = int(s[0])
            second_digit = int(s[1])
            if first_digit == 0:
                return self.NUMBER[second_digit]
            elif first_digit == 1:
                return self.NUMBER_TEEN[second_digit]
            else:
                return self.NUMBER_TEN[first_digit - 1] + " " + self.NUMBER[second_digit]
        elif len(s) == 1:
            return self.NUMBER[int(s)]
        else:
            return ""

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        if len(s) == 3:
            first_digit = int(s[0])
            second_digit = int(s[1])
            third_digit = int(s[2])
            if first_digit != 0:
                result = self.NUMBER[first_digit] + " HUNDRED"
                if second_digit != 0 or third_digit != 0:
                    result += " AND " + self.trans_two(s[1:])
                return result
            else:
                return self.trans_two(s[1:])
        elif len(s) == 2:
            return self.trans_two(s)
        elif len(s) == 1:
            return self.NUMBER[int(s)]
        else:
            return ""

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