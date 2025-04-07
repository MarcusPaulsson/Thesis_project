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
        """
        if x is None:
            return ""
        if x == 0:
            return "ZERO ONLY"
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = int(round((x - integer_part) * 100))
            return f"{self.number_to_words(integer_part)} AND CENTS {self.trans_two(str(decimal_part))} ONLY"
        return f"{self.number_to_words(int(x))} ONLY"

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        return self.format(float(x))

    def number_to_words(self, num):
        if num == 0:
            return ""
        elif num < 10:
            return self.NUMBER[num]
        elif num < 20:
            return self.NUMBER_TEEN[num - 10]
        elif num < 100:
            return self.trans_two(str(num))
        elif num < 1000:
            return self.trans_three(str(num))
        else:
            words = []
            for idx, scale in enumerate(self.NUMBER_MORE):
                if num % 1000 != 0:
                    words.append(self.number_to_words(num % 1000) + (" " + scale if scale else ""))
                num //= 1000
                if num == 0:
                    break
            return ' '.join(reversed(words)).strip()

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        n = int(s)
        if n < 10:
            return self.NUMBER[n]
        elif n < 20:
            return self.NUMBER_TEEN[n - 10]
        else:
            ten = self.NUMBER_TEN[n // 10 - 1]
            one = self.NUMBER[n % 10]
            return f"{ten} {one}".strip()

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        n = int(s)
        if n < 100:
            return self.trans_two(s)
        else:
            hundred = self.NUMBER[n // 100] + " HUNDRED"
            rest = self.trans_two(str(n % 100))
            return f"{hundred} AND {rest}".strip()

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        return self.NUMBER_MORE[i]