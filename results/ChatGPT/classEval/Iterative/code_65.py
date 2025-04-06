class NumberWordFormatter:
    """
    This is a class that converts numbers into their corresponding English word representation, 
    handling both integer and decimal parts, and incorporating appropriate connectors and units.
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
        Converts a number into words format.
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = int(round((x - integer_part) * 100))
            return self.format_integer(integer_part) + " POINT " + self.format_integer(decimal_part)
        elif isinstance(x, int):
            return self.format_integer(x)
        else:
            raise ValueError("Input must be an integer or float.")

    def format_string(self, x):
        """
        Converts a string representation of a number into words format.
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        return self.format(int(x))

    def trans_two(self, s):
        """
        Converts a two-digit number into words format.
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
            return self.NUMBER_TEN[ten - 1] + (" " + self.NUMBER[one] if one > 0 else "")

    def trans_three(self, s):
        """
        Converts a three-digit number into words format.
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        num = int(s)
        hundred = num // 100
        rest = num % 100
        result = self.NUMBER[hundred] + " HUNDRED"
        if rest > 0:
            result += " AND " + self.trans_two(f"{rest:02d}")
        return result.strip()

    def format_integer(self, num):
        """
        Converts an integer part of a number into words format.
        :param num: int, the integer part of the number
        :return: str, the integer in words format
        """
        if num == 0:
            return "ZERO"
        words = []
        index = 0
        while num > 0:
            part = num % 1000
            if part > 0:
                words.append(self.trans_three(f"{part:03d}") + (" " + self.NUMBER_MORE[index] if index > 0 else ""))
            num //= 1000
            index += 1
        return " AND ".join(reversed(words)).strip() + " ONLY"