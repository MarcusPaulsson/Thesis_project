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
        try:
            num = int(x)
        except ValueError:
            return "Invalid input: Input must be a number."

        if num == 0:
            return "ZERO ONLY"

        num_str = str(num)
        parts = []
        num_len = len(num_str)
        group_index = 0

        while num_len > 0:
            if num_len >= 3:
                three_digits = num_str[num_len - 3:num_len]
                num_len -= 3
            else:
                three_digits = num_str[0:num_len]
                num_len = 0

            if int(three_digits) != 0:
                parts.insert(0, self.trans_three(three_digits) + " " + self.NUMBER_MORE[group_index])
            group_index += 1

        result = " ".join(parts).strip()
        return result + " ONLY"

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
            num = int(x)
        except ValueError:
            return "Invalid input: Input must be a number string."

        return self.format(num)

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

        if s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        elif s[0] == '0':
            return self.NUMBER[int(s[1])]
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

        hundred = int(s[0])
        rest = s[1:3]
        result = ""

        if hundred > 0:
            result += self.NUMBER[hundred] + " HUNDRED"
            if int(rest) > 0:
                result += " AND "

        result += self.trans_two(rest)
        return result.strip()

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