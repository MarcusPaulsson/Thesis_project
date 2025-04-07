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
            return self.format(integer_part) + " AND CENTS " + self.trans_two(str(decimal_part).zfill(2)) + " ONLY"
        elif x == 0:
            return "ZERO ONLY"
        else:
            return self.convert_number(x) + " ONLY"

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
            num = float(x)
            return self.format(num)
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
        if len(s) == 1:
            return self.NUMBER[int(s)]
        elif s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            return self.NUMBER_TEN[int(s[0]) - 1] + " " + self.NUMBER[int(s[1])]

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        if len(s) == 1:
            return self.NUMBER[int(s)]
        elif len(s) == 2:
            return self.trans_two(s)
        else:
            if s[1] == '0' and s[2] == '0':
                return self.NUMBER[int(s[0])] + " HUNDRED"
            elif s[1] == '0':
                return self.NUMBER[int(s[0])] + " HUNDRED AND " + self.NUMBER[int(s[2])]
            else:
                return self.NUMBER[int(s[0])] + " HUNDRED AND " + self.trans_two(s[1:])

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

    def convert_number(self, num):
        """
        Converts a number into words format
        :param num: int, the number to be converted into words format
        :return: str, the number in words format
        """
        num_str = str(num)
        length = len(num_str)
        result = []
        for i in range(length):
            digit = int(num_str[i])
            if digit != 0:
                result.append(self.NUMBER[digit])
        if length == 1:
            return " ".join(result)
        elif length == 2:
            return self.trans_two(num_str)
        elif length == 3:
            return self.trans_three(num_str)
        else:
            parts = []
            for i in range(length - 1, -1, -3):
                start = max(0, i - 2)
                part = num_str[start:i + 1]
                if part:
                    parts.insert(0, self.trans_three(part))
            result = " ".join(parts)
            return result