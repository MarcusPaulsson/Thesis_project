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
        if isinstance(x, float):
            integer_part = str(int(x))
            decimal_part = str(int((x - int(x)) * 100))
            return f"{self._convert_integer_to_words(integer_part)} POINT {self._convert_integer_to_words(decimal_part)} ONLY"
        else:
            return f"{self._convert_integer_to_words(str(x))} ONLY"

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
        elif 10 <= num < 20:
            return self.NUMBER_TEEN[num - 10]
        else:
            ten = num // 10
            one = num % 10
            return f"{self.NUMBER_TEN[ten - 1]} {self.NUMBER[one]}".strip()

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
        hundred = num // 100
        rest = num % 100
        if hundred > 0:
            if rest > 0:
                return f"{self.NUMBER[hundred]} HUNDRED AND {self.trans_two(str(rest))}"
            else:
                return f"{self.NUMBER[hundred]} HUNDRED"
        else:
            return self.trans_two(str(rest))

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

    def _convert_integer_to_words(self, integer_part):
        """
        Converts an integer part into words format
        :param integer_part: str, the integer part of the number
        :return: str, the number in words format
        """
        num = int(integer_part)
        if num == 0:
            return "ZERO"
        
        words = []
        index = 0

        while num > 0:
            chunk = num % 1000
            if chunk > 0:
                words.append(f"{self.trans_three(str(chunk))} {self.parse_more(index)}")
            num //= 1000
            index += 1
        
        return ' '.join(reversed(words)).strip()