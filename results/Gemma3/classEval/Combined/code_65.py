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
        if x == 0:
            return "ZERO ONLY"

        result = ""
        i = 0
        while x > 0:
            remainder = x % 1000
            if remainder > 0:
                result = self.trans_three(str(remainder).zfill(3)) + " " + self.NUMBER_MORE[i] + " " + result
            x //= 1000
            i += 1
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
            if s[0] != '0':
                result = self.NUMBER[int(s[0])] + " HUNDRED"
                if int(s[1:]) > 0:
                    result += " AND " + self.trans_two(s[1:])
                return result
            else:
                return self.trans_two(s[1:])