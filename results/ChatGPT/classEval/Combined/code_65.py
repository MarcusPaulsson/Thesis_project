class NumberWordFormatter:
    """
    A class that converts numbers into their corresponding English word representation,
    handling both integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.units = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                      "EIGHTEEN", "NINETEEN"]
        self.tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.magnitudes = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, x):
        """
        Converts a number into words format.
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        """
        if x is None:
            return ""
        elif x == 0:
            return "ZERO ONLY"
        
        integer_part = int(x)
        decimal_part = round((x - integer_part) * 100)

        words = self.format_integer(integer_part)
        if decimal_part > 0:
            words += f" AND CENTS {self.trans_two(str(decimal_part))} ONLY"
        else:
            words += " ONLY"
        return words

    def format_string(self, x):
        """
        Converts a string representation of a number into words format.
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        return self.format(float(x))

    def trans_two(self, s):
        """
        Converts a two-digit number into words format.
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        n = int(s)
        if n < 10:
            return self.units[n]
        elif n < 20:
            return self.teens[n - 10]
        else:
            return self.tens[n // 10] + ('' if n % 10 == 0 else ' ' + self.units[n % 10])

    def trans_three(self, s):
        """
        Converts a three-digit number into words format.
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        n = int(s)
        if n == 0:
            return ""
        elif n < 100:
            return self.trans_two(s)
        else:
            return self.units[n // 100] + " HUNDRED" + ('' if n % 100 == 0 else ' AND ' + self.trans_two(str(n % 100)))

    def format_integer(self, n):
        """
        Formats an integer into words.
        :param n: int, the integer to be converted
        :return: str, the number in words format
        """
        if n == 0:
            return "ZERO"

        parts = []
        magnitude_index = 0

        while n > 0:
            if n % 1000 != 0:
                part = self.trans_three(str(n % 1000))
                if magnitude_index > 0:
                    part += " " + self.magnitudes[magnitude_index]
                parts.append(part)
            n //= 1000
            magnitude_index += 1

        return ' '.join(reversed(parts)).strip()