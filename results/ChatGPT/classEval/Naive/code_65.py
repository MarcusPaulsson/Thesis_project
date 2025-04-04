class NumberWordFormatter:
    """
    This class converts numbers into their corresponding English word representation, 
    handling both integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", 
                            "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", 
                           "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        
    def format(self, x):
        """
        Converts a number into words format.
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        """
        if isinstance(x, str):
            x = float(x)
        integer_part, decimal_part = str(x).split('.') if '.' in str(x) else (str(x), None)
        words = self.convert_integer_part(integer_part)
        if decimal_part:
            words += " POINT " + " ".join(self.NUMBER[int(digit)] for digit in decimal_part)
        return words.strip() + " ONLY"

    def format_string(self, x):
        """
        Converts a string representation of a number into words format.
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        return self.format(float(x))

    def convert_integer_part(self, num):
        """
        Converts the integer part of a number into words format.
        :param num: str, the integer part of the number
        :return: str, the number in words format
        """
        num = int(num)
        if num == 0:
            return "ZERO"
        
        words = ""
        for idx, chunk in enumerate(self.chunk_number(num)):
            if chunk > 0:
                words = self.trans_three(chunk) + " " + self.NUMBER_MORE[idx] + " " + words
        
        return words.strip()

    def chunk_number(self, num):
        """
        Breaks the number into chunks of three digits.
        :param num: int, the number to chunk
        :return: list of int, the chunks
        """
        chunks = []
        while num > 0:
            chunks.append(num % 1000)
            num //= 1000
        return chunks

    def trans_two(self, s):
        """
        Converts a two-digit number into words format.
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        n = int(s)
        if n < 10:
            return self.NUMBER[n]
        elif n < 20:
            return self.NUMBER_TEEN[n - 10]
        else:
            ten = n // 10
            one = n % 10
            return self.NUMBER_TEN[ten - 1] + (" " + self.NUMBER[one] if one > 0 else "")

    def trans_three(self, s):
        """
        Converts a three-digit number into words format.
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        n = int(s)
        hundred = n // 100
        rest = n % 100
        words = ""
        if hundred > 0:
            words += self.NUMBER[hundred] + " HUNDRED"
        if rest > 0:
            if hundred > 0:
                words += " AND "
            words += self.trans_two(rest)
        return words.strip()

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index.
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        return self.NUMBER_MORE[i]