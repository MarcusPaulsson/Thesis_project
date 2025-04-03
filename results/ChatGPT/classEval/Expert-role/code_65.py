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
        if isinstance(x, int):
            return self.format_integer(x) + " ONLY"
        elif isinstance(x, float):
            integer_part = int(x)
            decimal_part = round((x - integer_part) * 100)
            return self.format_integer(integer_part) + " AND " + self.format_integer(decimal_part) + " CENTS ONLY"
        else:
            raise ValueError("Input must be an integer or float")

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
            ten_part = self.NUMBER_TEN[num // 10 - 1]
            one_part = self.NUMBER[num % 10]
            return ten_part + (" " + one_part if one_part else "")

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
        if num < 100:
            return self.trans_two(s)
        else:
            hundred_part = self.NUMBER[num // 100] + " HUNDRED"
            remainder = num % 100
            return hundred_part + (" AND " + self.trans_two(str(remainder)) if remainder else "")

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
    
    def format_integer(self, num):
        if num == 0:
            return "ZERO"
        words = ""
        index = 0
        while num > 0:
            part = num % 1000
            if part > 0:
                words = self.trans_three(str(part)) + (" " + self.parse_more(index) if index > 0 else "") + (" " + words if words else "")
            num //= 1000
            index += 1
        return words.strip()