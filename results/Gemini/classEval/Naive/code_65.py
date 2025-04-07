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
            decimal_part = round((x - integer_part) * 100)
            integer_words = self.format(integer_part)
            decimal_words = self.trans_two(str(decimal_part).zfill(2))
            if integer_words == "ZERO ONLY":
                return "ZERO AND CENTS " + decimal_words + " ONLY"
            return integer_words.replace("ONLY", "") + " AND CENTS " + decimal_words + " ONLY"
        if x == 0:
            return "ZERO ONLY"
        s = str(int(x))
        length = len(s)
        result = []
        i = length - 1
        j = 0
        while i >= 0:
            temp = ""
            if i >= 2:
                temp = self.trans_three(s[i - 2:i + 1])
                i -= 3
            elif i == 1:
                temp = self.trans_two(s[i - 1:i + 1])
                i -= 2
            else:
                temp = self.NUMBER[int(s[i])]
                i -= 1
            if temp != "":
                result.append(temp + " " + self.parse_more(j))
            j += 1
        result.reverse()
        return " ".join(result).strip() + " ONLY"

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
            return self.NUMBER[int(s[1])]
        elif s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            if s[1] == '0':
                return self.NUMBER_TEN[int(s[0]) - 1]
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
        result = []
        if s[0] != '0':
            result.append(self.NUMBER[int(s[0])])
            result.append("HUNDRED")
        two_digits = self.trans_two(s[1:])
        if two_digits != "":
            if len(result) > 0:
                result.append("AND")
            result.append(two_digits)
        return " ".join(result).strip()

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