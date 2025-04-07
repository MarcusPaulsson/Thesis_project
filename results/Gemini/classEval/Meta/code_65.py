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
                return f"ZERO AND CENTS {decimal_words} ONLY"
            else:
                return f"{integer_words.replace(' ONLY', '')} AND CENTS {decimal_words} ONLY"

        if x == 0:
            return "ZERO ONLY"

        x = int(x)
        num_str = str(x)
        num_len = len(num_str)
        words = []
        group_index = 0

        while num_len > 0:
            group = num_str[max(0, num_len - 3):num_len]
            num_len -= 3

            if int(group) != 0:
                three_words = self.trans_three(group)
                more_word = self.parse_more(group_index)
                if more_word:
                    words.insert(0, f"{three_words} {more_word}")
                else:
                    words.insert(0, three_words)

            group_index += 1

        return " ".join(words).strip() + " ONLY"


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
        elif s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            ten_index = int(s[0]) - 1
            one_index = int(s[1])
            if one_index == 0:
                return self.NUMBER_TEN[ten_index]
            else:
                return f"{self.NUMBER_TEN[ten_index]} {self.NUMBER[one_index]}"


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

        hundred_digit = int(s[0])
        rest_of_number = s[1:]

        words = []

        if hundred_digit != 0:
            words.append(f"{self.NUMBER[hundred_digit]} HUNDRED")

        two_digit_words = self.trans_two(rest_of_number)

        if two_digit_words:
            if words:
                words.append("AND")
            words.append(two_digit_words)

        return " ".join(words).strip()

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        if 0 <= i < len(self.NUMBER_MORE):
            return self.NUMBER_MORE[i]
        else:
            return ""