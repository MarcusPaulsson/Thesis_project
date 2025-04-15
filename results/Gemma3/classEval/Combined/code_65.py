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
        """
        if x is None:
            return ""
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = int(round((x - integer_part) * 100))
            return self._format_integer(integer_part) + " AND CENTS " + self.trans_two(str(decimal_part).zfill(2)) + " ONLY"
        elif x == 0:
            return "ZERO ONLY"
        else:
            return self._format_integer(x) + " ONLY"

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
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
        """
        return self.NUMBER_MORE[i]

    def _format_integer(self, x):
        """
        Helper function to format the integer part of the number.
        """
        s = str(x)
        n = len(s)
        result = []
        for i in range(n):
            digit = int(s[i])
            if digit != 0:
                result.append(self.NUMBER[digit])

        if not result:
            return ""

        formatted_number = ""
        group_count = 0
        temp_list = []
        for i in range(n - 1, -1, -1):
            temp_list.insert(0, s[i])
            group_count += 1
            if group_count == 3 and i != 0:
                formatted_number = self.parse_more((n - len(temp_list)) // 3) + " " + self.trans_three("".join(temp_list)) + " " + formatted_number
                temp_list = []
                group_count = 0

        formatted_number = self.trans_three("".join(temp_list)) + " " + formatted_number
        return formatted_number.strip()