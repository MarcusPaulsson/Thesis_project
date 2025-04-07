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
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if x is None:
            return ""
        if isinstance(x, int) or isinstance(x, float):
            integer_part = int(x)
            decimal_part = round((x - integer_part) * 100)
            result = self.convert_integer(integer_part)
            if decimal_part > 0:
                result += " AND CENTS " + self.trans_two(str(decimal_part))
            return result + " ONLY"
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
        if x.isdigit() or (x.replace('.', '', 1).isdigit() and x.count('.') < 2):
            return self.format(float(x))
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
        if s[0] == '1' and s[1] != '0':
            return self.NUMBER_TEEN[int(s[1])]
        elif s[0] == '0':
            return self.NUMBER[int(s[1])]
        else:
            return self.NUMBER_TEN[int(s[0]) - 1] + (" " + self.NUMBER[int(s[1])] if s[1] != '0' else "")

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        if s[0] != '0':
            return self.NUMBER[int(s[0])] + " HUNDRED" + (" AND " + self.trans_two(s[1:]) if s[1:] != "00" else "")
        else:
            return self.trans_two(s[1:])

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

    def convert_integer(self, num):
        if num == 0:
            return "ZERO"
        parts = []
        thousands = 0
        while num > 0:
            part = num % 1000
            if part > 0:
                if thousands > 0:
                    parts.append(self.parse_more(thousands))
                parts.append(self.trans_three(str(part).zfill(3)))
            num //= 1000
            thousands += 1
        return ' AND '.join(reversed(parts))