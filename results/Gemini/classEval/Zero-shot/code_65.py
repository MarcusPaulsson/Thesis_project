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
            integer_words = self.format(integer_part)
            decimal_words = self.format(decimal_part)

            if integer_part == 0 and decimal_part == 0:
                return "ZERO ONLY"

            if integer_words == "ZERO ONLY":
                integer_words = "ZERO"

            if integer_part != 0 and decimal_part != 0:
                return f"{integer_words.replace('ONLY', '')} AND CENTS {decimal_words.replace('ONLY', '')} ONLY"
            elif integer_part != 0:
                return f"{integer_words.replace('ONLY', '')} ONLY"
            else:
                return f"{decimal_words.replace('ONLY', '')} ONLY"

        if x == 0:
            return "ZERO ONLY"

        x = int(x)
        parts = []
        i = 0
        while x > 0:
            n = x % 1000
            if n != 0:
                part = self.trans_three(str(n).zfill(3))
                if i > 0:
                    part += " " + self.parse_more(i)
                parts.append(part)
            x //= 1000
            i += 1

        parts.reverse()
        result = " ".join(parts)
        return result.strip() + " ONLY"

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
        if len(s) != 2:
            return ""

        if s[0] == '0':
            if s[1] == '0':
                return ""
            else:
                return self.NUMBER[int(s[1])]

        if s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            if s[1] == '0':
                return self.NUMBER_TEN[int(s[0] )-1]
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
        if len(s) != 3:
            return ""

        res = ""
        if s[0] != '0':
            res += self.NUMBER[int(s[0])] + " HUNDRED"

        two_digit = s[1:]
        two_digit_words = self.trans_two(two_digit)

        if res and two_digit_words:
            res += " AND " + two_digit_words
        elif two_digit_words:
            res += two_digit_words

        return res

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